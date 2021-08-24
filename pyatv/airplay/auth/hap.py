"""API for performing and verifying device authentication."""
from copy import copy
import logging
from typing import Any, Dict, Tuple

from pyatv import exceptions
from pyatv.auth import hap_tlv8
from pyatv.auth.hap_pairing import (
    HapCredentials,
    PairSetupProcedure,
    PairVerifyProcedure,
)
from pyatv.auth.hap_srp import SRPAuthHandler
from pyatv.support import log_binary
from pyatv.support.http import HttpConnection, HttpResponse

_LOGGER = logging.getLogger(__name__)

_AIRPLAY_HEADERS = {
    "User-Agent": "AirPlay/320.20",
    "Connection": "keep-alive",
    "X-Apple-HKP": 3,
    "Content-Type": "application/octet-stream",
}


SRP_SALT = "Control-Salt"
SRP_OUTPUT_INFO = "Control-Write-Encryption-Key"
SRP_INPUT_INFO = "Control-Read-Encryption-Key"


class AirPlayHapPairSetupProcedure(PairSetupProcedure):
    """Authenticate a device for AirPlay playback."""

    def __init__(self, http: HttpConnection, auth_handler: SRPAuthHandler):
        """Initialize a new DeviceAuthenticator."""
        self.http = http
        self.srp = auth_handler
        self._atv_salt = None
        self._atv_pub_key = None

    async def start_pairing(self) -> None:
        """Start the authentication process.

        This method will show the expected PIN on screen.
        """
        self.srp.initialize()

        await self.http.post("/pair-pin-start", headers=_AIRPLAY_HEADERS)

        data = {hap_tlv8.TlvValue.Method: b"\x00", hap_tlv8.TlvValue.SeqNo: b"\x01"}
        resp = await self.http.post(
            "/pair-setup", body=hap_tlv8.write_tlv(data), headers=_AIRPLAY_HEADERS
        )
        pairing_data = hap_tlv8.read_tlv(resp.body)

        self._atv_salt = pairing_data[hap_tlv8.TlvValue.Salt]
        self._atv_pub_key = pairing_data[hap_tlv8.TlvValue.PublicKey]

    async def finish_pairing(self, username: str, pin_code: int) -> bool:
        """Finish authentication process.

        A username (generated by new_credentials) and the PIN code shown on
        screen must be provided.
        """
        # Step 1
        self.srp.step1(pin_code)

        pub_key, proof = self.srp.step2(self._atv_pub_key, self._atv_salt)
        data = {
            hap_tlv8.TlvValue.SeqNo: b"\x03",
            hap_tlv8.TlvValue.PublicKey: pub_key,
            hap_tlv8.TlvValue.Proof: proof,
        }
        await self.http.post(
            "/pair-setup", body=hap_tlv8.write_tlv(data), headers=_AIRPLAY_HEADERS
        )

        data = {
            hap_tlv8.TlvValue.SeqNo: b"\x05",
            hap_tlv8.TlvValue.EncryptedData: self.srp.step3(),
        }
        resp = await self.http.post(
            "/pair-setup", body=hap_tlv8.write_tlv(data), headers=_AIRPLAY_HEADERS
        )
        pairing_data = hap_tlv8.read_tlv(resp.body)

        encrypted_data = pairing_data[hap_tlv8.TlvValue.EncryptedData]
        return self.srp.step4(encrypted_data)


class AirPlayHapPairVerifyProcedure(PairVerifyProcedure):
    """Verify if a device is allowed to perform AirPlay playback."""

    def __init__(
        self,
        http: HttpConnection,
        auth_handler: SRPAuthHandler,
        credentials: HapCredentials,
    ):
        """Initialize a new AuthenticationVerifier."""
        self.http = http
        self.srp = auth_handler
        self.credentials = credentials
        self._output_key = None
        self._input_key = None

    async def verify_credentials(self) -> bool:
        """Verify if device is allowed to use AirPlau."""

        _, public_key = self.srp.initialize()

        resp = await self._send(
            {
                hap_tlv8.TlvValue.SeqNo: b"\x01",
                hap_tlv8.TlvValue.PublicKey: public_key,
            }
        )

        pairing_data = hap_tlv8.read_tlv(resp.body)
        session_pub_key = pairing_data[hap_tlv8.TlvValue.PublicKey]
        encrypted = pairing_data[hap_tlv8.TlvValue.EncryptedData]
        log_binary(_LOGGER, "Device", Public=self.credentials.ltpk, Encrypted=encrypted)

        encrypted_data = self.srp.verify1(self.credentials, session_pub_key, encrypted)
        await self._send(
            {
                hap_tlv8.TlvValue.SeqNo: b"\x03",
                hap_tlv8.TlvValue.EncryptedData: encrypted_data,
            }
        )

        # TODO: check status code

        self._output_key, self._input_key = self.srp.verify2(
            SRP_SALT, SRP_OUTPUT_INFO, SRP_INPUT_INFO
        )

        log_binary(
            _LOGGER,
            "Got encryption keys",
            Input=self._input_key,
            Output=self._output_key,
        )
        return True

    async def _send(self, data: Dict[Any, Any]) -> HttpResponse:
        headers = copy(_AIRPLAY_HEADERS)
        headers["Content-Type"] = "application/octet-stream"
        return await self.http.post(
            "/pair-verify", body=hap_tlv8.write_tlv(data), headers=headers
        )

    def encryption_keys(self) -> Tuple[str, str]:
        """Return derived encryption keys."""
        if self._output_key is None or self._input_key is None:
            raise exceptions.NoCredentialsError("verification has not succeeded")
        return self._output_key, self._input_key

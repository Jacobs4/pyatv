"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetVolumeMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OUTPUTDEVICEUID_FIELD_NUMBER: builtins.int
    outputDeviceUID: typing.Text = ...
    def __init__(self,
        *,
        outputDeviceUID : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"outputDeviceUID",b"outputDeviceUID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"outputDeviceUID",b"outputDeviceUID"]) -> None: ...
global___GetVolumeMessage = GetVolumeMessage

getVolumeMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___GetVolumeMessage] = ...
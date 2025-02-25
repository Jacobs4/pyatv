"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.Common_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CommandOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SOURCEID_FIELD_NUMBER: builtins.int
    MEDIATYPE_FIELD_NUMBER: builtins.int
    EXTERNALPLAYERCOMMAND_FIELD_NUMBER: builtins.int
    SKIPINTERVAL_FIELD_NUMBER: builtins.int
    PLAYBACKRATE_FIELD_NUMBER: builtins.int
    RATING_FIELD_NUMBER: builtins.int
    NEGATIVE_FIELD_NUMBER: builtins.int
    PLAYBACKPOSITION_FIELD_NUMBER: builtins.int
    REPEATMODE_FIELD_NUMBER: builtins.int
    SHUFFLEMODE_FIELD_NUMBER: builtins.int
    TRACKID_FIELD_NUMBER: builtins.int
    RADIOSTATIONID_FIELD_NUMBER: builtins.int
    RADIOSTATIONHASH_FIELD_NUMBER: builtins.int
    SYSTEMAPPPLAYBACKQUEUEDATA_FIELD_NUMBER: builtins.int
    DESTINATIONAPPDISPLAYID_FIELD_NUMBER: builtins.int
    SENDOPTIONS_FIELD_NUMBER: builtins.int
    REQUESTDEFERMENTTOPLAYBACKQUEUEPOSITION_FIELD_NUMBER: builtins.int
    CONTEXTID_FIELD_NUMBER: builtins.int
    SHOULDOVERRIDEMANUALLYCURATEDQUEUE_FIELD_NUMBER: builtins.int
    STATIONURL_FIELD_NUMBER: builtins.int
    SHOULDBEGINRADIOPLAYBACK_FIELD_NUMBER: builtins.int
    PLAYBACKQUEUEINSERTIONPOSITION_FIELD_NUMBER: builtins.int
    CONTENTITEMID_FIELD_NUMBER: builtins.int
    PLAYBACKQUEUEOFFSET_FIELD_NUMBER: builtins.int
    PLAYBACKQUEUEDESTINATIONOFFSET_FIELD_NUMBER: builtins.int
    LANGUAGEOPTION_FIELD_NUMBER: builtins.int
    PLAYBACKQUEUECONTEXT_FIELD_NUMBER: builtins.int
    INSERTAFTERCONTENTITEMID_FIELD_NUMBER: builtins.int
    NOWPLAYINGCONTENTITEMID_FIELD_NUMBER: builtins.int
    REPLACEINTENT_FIELD_NUMBER: builtins.int
    sourceId: typing.Text = ...
    mediaType: typing.Text = ...
    externalPlayerCommand: builtins.bool = ...
    skipInterval: builtins.float = ...
    playbackRate: builtins.float = ...
    rating: builtins.float = ...
    negative: builtins.bool = ...
    playbackPosition: builtins.float = ...
    repeatMode: pyatv.protocols.mrp.protobuf.Common_pb2.RepeatMode.Enum.V = ...
    shuffleMode: pyatv.protocols.mrp.protobuf.Common_pb2.ShuffleMode.Enum.V = ...
    trackID: builtins.int = ...
    radioStationID: builtins.int = ...
    radioStationHash: typing.Text = ...
    systemAppPlaybackQueueData: builtins.bytes = ...
    destinationAppDisplayID: typing.Text = ...
    sendOptions: builtins.int = ...
    requestDefermentToPlaybackQueuePosition: builtins.bool = ...
    contextID: typing.Text = ...
    shouldOverrideManuallyCuratedQueue: builtins.bool = ...
    stationURL: typing.Text = ...
    shouldBeginRadioPlayback: builtins.bool = ...
    playbackQueueInsertionPosition: builtins.int = ...
    contentItemID: typing.Text = ...
    playbackQueueOffset: builtins.int = ...
    playbackQueueDestinationOffset: builtins.int = ...
    languageOption: builtins.bytes = ...
    playbackQueueContext: builtins.bytes = ...
    insertAfterContentItemID: typing.Text = ...
    nowPlayingContentItemID: typing.Text = ...
    replaceIntent: builtins.int = ...
    def __init__(self,
        *,
        sourceId : typing.Optional[typing.Text] = ...,
        mediaType : typing.Optional[typing.Text] = ...,
        externalPlayerCommand : typing.Optional[builtins.bool] = ...,
        skipInterval : typing.Optional[builtins.float] = ...,
        playbackRate : typing.Optional[builtins.float] = ...,
        rating : typing.Optional[builtins.float] = ...,
        negative : typing.Optional[builtins.bool] = ...,
        playbackPosition : typing.Optional[builtins.float] = ...,
        repeatMode : typing.Optional[pyatv.protocols.mrp.protobuf.Common_pb2.RepeatMode.Enum.V] = ...,
        shuffleMode : typing.Optional[pyatv.protocols.mrp.protobuf.Common_pb2.ShuffleMode.Enum.V] = ...,
        trackID : typing.Optional[builtins.int] = ...,
        radioStationID : typing.Optional[builtins.int] = ...,
        radioStationHash : typing.Optional[typing.Text] = ...,
        systemAppPlaybackQueueData : typing.Optional[builtins.bytes] = ...,
        destinationAppDisplayID : typing.Optional[typing.Text] = ...,
        sendOptions : typing.Optional[builtins.int] = ...,
        requestDefermentToPlaybackQueuePosition : typing.Optional[builtins.bool] = ...,
        contextID : typing.Optional[typing.Text] = ...,
        shouldOverrideManuallyCuratedQueue : typing.Optional[builtins.bool] = ...,
        stationURL : typing.Optional[typing.Text] = ...,
        shouldBeginRadioPlayback : typing.Optional[builtins.bool] = ...,
        playbackQueueInsertionPosition : typing.Optional[builtins.int] = ...,
        contentItemID : typing.Optional[typing.Text] = ...,
        playbackQueueOffset : typing.Optional[builtins.int] = ...,
        playbackQueueDestinationOffset : typing.Optional[builtins.int] = ...,
        languageOption : typing.Optional[builtins.bytes] = ...,
        playbackQueueContext : typing.Optional[builtins.bytes] = ...,
        insertAfterContentItemID : typing.Optional[typing.Text] = ...,
        nowPlayingContentItemID : typing.Optional[typing.Text] = ...,
        replaceIntent : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"contentItemID",b"contentItemID",u"contextID",b"contextID",u"destinationAppDisplayID",b"destinationAppDisplayID",u"externalPlayerCommand",b"externalPlayerCommand",u"insertAfterContentItemID",b"insertAfterContentItemID",u"languageOption",b"languageOption",u"mediaType",b"mediaType",u"negative",b"negative",u"nowPlayingContentItemID",b"nowPlayingContentItemID",u"playbackPosition",b"playbackPosition",u"playbackQueueContext",b"playbackQueueContext",u"playbackQueueDestinationOffset",b"playbackQueueDestinationOffset",u"playbackQueueInsertionPosition",b"playbackQueueInsertionPosition",u"playbackQueueOffset",b"playbackQueueOffset",u"playbackRate",b"playbackRate",u"radioStationHash",b"radioStationHash",u"radioStationID",b"radioStationID",u"rating",b"rating",u"repeatMode",b"repeatMode",u"replaceIntent",b"replaceIntent",u"requestDefermentToPlaybackQueuePosition",b"requestDefermentToPlaybackQueuePosition",u"sendOptions",b"sendOptions",u"shouldBeginRadioPlayback",b"shouldBeginRadioPlayback",u"shouldOverrideManuallyCuratedQueue",b"shouldOverrideManuallyCuratedQueue",u"shuffleMode",b"shuffleMode",u"skipInterval",b"skipInterval",u"sourceId",b"sourceId",u"stationURL",b"stationURL",u"systemAppPlaybackQueueData",b"systemAppPlaybackQueueData",u"trackID",b"trackID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"contentItemID",b"contentItemID",u"contextID",b"contextID",u"destinationAppDisplayID",b"destinationAppDisplayID",u"externalPlayerCommand",b"externalPlayerCommand",u"insertAfterContentItemID",b"insertAfterContentItemID",u"languageOption",b"languageOption",u"mediaType",b"mediaType",u"negative",b"negative",u"nowPlayingContentItemID",b"nowPlayingContentItemID",u"playbackPosition",b"playbackPosition",u"playbackQueueContext",b"playbackQueueContext",u"playbackQueueDestinationOffset",b"playbackQueueDestinationOffset",u"playbackQueueInsertionPosition",b"playbackQueueInsertionPosition",u"playbackQueueOffset",b"playbackQueueOffset",u"playbackRate",b"playbackRate",u"radioStationHash",b"radioStationHash",u"radioStationID",b"radioStationID",u"rating",b"rating",u"repeatMode",b"repeatMode",u"replaceIntent",b"replaceIntent",u"requestDefermentToPlaybackQueuePosition",b"requestDefermentToPlaybackQueuePosition",u"sendOptions",b"sendOptions",u"shouldBeginRadioPlayback",b"shouldBeginRadioPlayback",u"shouldOverrideManuallyCuratedQueue",b"shouldOverrideManuallyCuratedQueue",u"shuffleMode",b"shuffleMode",u"skipInterval",b"skipInterval",u"sourceId",b"sourceId",u"stationURL",b"stationURL",u"systemAppPlaybackQueueData",b"systemAppPlaybackQueueData",u"trackID",b"trackID"]) -> None: ...
global___CommandOptions = CommandOptions

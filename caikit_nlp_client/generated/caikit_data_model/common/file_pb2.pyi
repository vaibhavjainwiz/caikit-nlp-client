from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ["data", "filename", "type"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    filename: str
    type: str
    def __init__(self, data: _Optional[bytes] = ..., filename: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

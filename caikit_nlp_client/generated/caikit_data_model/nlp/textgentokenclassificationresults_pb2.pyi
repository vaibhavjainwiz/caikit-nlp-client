from caikit_nlp_client.generated.caikit_data_model.nlp import tokenclassificationresult_pb2 as _tokenclassificationresult_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextGenTokenClassificationResults(_message.Message):
    __slots__ = ["input", "output"]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    input: _containers.RepeatedCompositeFieldContainer[_tokenclassificationresult_pb2.TokenClassificationResult]
    output: _containers.RepeatedCompositeFieldContainer[_tokenclassificationresult_pb2.TokenClassificationResult]
    def __init__(self, input: _Optional[_Iterable[_Union[_tokenclassificationresult_pb2.TokenClassificationResult, _Mapping]]] = ..., output: _Optional[_Iterable[_Union[_tokenclassificationresult_pb2.TokenClassificationResult, _Mapping]]] = ...) -> None: ...

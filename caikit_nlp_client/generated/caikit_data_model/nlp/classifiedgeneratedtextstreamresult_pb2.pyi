from caikit_nlp_client.generated.caikit_data_model.nlp import finishreason_pb2 as _finishreason_pb2
from caikit_nlp_client.generated.caikit_data_model.nlp import textgentokenclassificationresults_pb2 as _textgentokenclassificationresults_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClassifiedGeneratedTextStreamResult(_message.Message):
    __slots__ = ["generated_text", "token_classification_results", "finish_reason", "generated_token_count", "seed", "input_token_count", "processed_index"]
    GENERATED_TEXT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CLASSIFICATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    GENERATED_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROCESSED_INDEX_FIELD_NUMBER: _ClassVar[int]
    generated_text: str
    token_classification_results: _textgentokenclassificationresults_pb2.TextGenTokenClassificationResults
    finish_reason: _finishreason_pb2.FinishReason
    generated_token_count: int
    seed: int
    input_token_count: int
    processed_index: int
    def __init__(self, generated_text: _Optional[str] = ..., token_classification_results: _Optional[_Union[_textgentokenclassificationresults_pb2.TextGenTokenClassificationResults, _Mapping]] = ..., finish_reason: _Optional[_Union[_finishreason_pb2.FinishReason, str]] = ..., generated_token_count: _Optional[int] = ..., seed: _Optional[int] = ..., input_token_count: _Optional[int] = ..., processed_index: _Optional[int] = ...) -> None: ...

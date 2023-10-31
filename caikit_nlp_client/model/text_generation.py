from enum import Enum
from dataclasses import dataclass
from typing import Optional


class FinishReason(Enum):
    NOT_FINISHED: 1
    MAX_TOKENS: 2
    EOS_TOKEN: 3
    CANCELLED: 4
    TIME_LIMIT: 5
    STOP_SEQUENCE: 6
    TOKEN_LIMIT: 7
    ERROR: 8


@dataclass
class ProducerId:
    name: str
    version: str


@dataclass
class TextGenerationTaskResult:
    generated_text: str
    """
    generated_tokens: int
    finish_reason: FinishReason
    producer_id: ProducerId
    input_token_count: int
    seed: int
    """


@dataclass
class ExponentialDecayLengthPenalty:
    start_index: int
    decay_factor: float


@dataclass
class TextGenerationTask:
    text: str
    max_new_tokens: Optional[int] = 200
    min_new_tokens: Optional[int] = 10
    preserve_input_text: Optional[bool] = False
    truncate_input_tokens: Optional[int] = None
    decoding_method: Optional[str] = None
    top_k: Optional[int] = None
    top_p: Optional[float] = None
    typical_p: Optional[float] = None
    temperature: Optional[float] = None
    seed: Optional[int] = None
    repetition_penalty: Optional[float] = None
    max_time: Optional[float] = None
    exponential_decay_length_penalty: Optional[ExponentialDecayLengthPenalty] = None
    stop_sequences: Optional[str] = None

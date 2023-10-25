from enum import Enum

class FinishReason(Enum):
    NOT_FINISHED: 1
    MAX_TOKENS: 2
    EOS_TOKEN: 3
    CANCELLED: 4
    TIME_LIMIT: 5
    STOP_SEQUENCE: 6
    TOKEN_LIMIT: 7
    ERROR: 8

class ProducerId:
    name: str
    version: str
class TextGenerationTaskResult:
    generated_text: str
    generated_tokens: int
    finish_reason: FinishReason
    producer_id: ProducerId
    input_token_count: int
    seed: int

class TextGenerationTaskRequest:
    text: str
    max_new_tokens: int
    min_new_tokens: int
    truncate_input_tokens: int
    decoding_method: str
    top_k: int
    top_p: float
    typical_p: float
    temperature: float
    seed: int
    repetition_penalty: float
    max_time: float
    # exponential_decay_length_penalty: _exponentialdecaylengthpenalty_pb2.ExponentialDecayLengthPenalty
    # stop_sequences: _containers.RepeatedScalarFieldContainer[str]
    preserve_input_text: bool

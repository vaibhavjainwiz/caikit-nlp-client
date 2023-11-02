import pytest
from caikit_nlp_client.grpc_client_introspection import GrpcCaikitNlpClientIntrospection


@pytest.fixture
def connected_client(channel):
    """Returns returns a grpc client connected to a locally running server"""
    return GrpcCaikitNlpClientIntrospection(channel)


def test_generate_text(connected_client):
    generated_text = connected_client.generate_text(
        "flan-t5-small-caikit", "What does foobar mean?"
    )
    assert generated_text == "a symphony"


def test_generate_text_with_optional_args(connected_client):
    generated_text = connected_client.generate_text(
        "flan-t5-small-caikit",
        "What does foobar mean?",
        preserve_input_text=False,
        max_new_tokens=20,
        min_new_tokens=4,
    )
    assert generated_text == "a symphony"


def test_generate_text_with_no_model_id(connected_client):
    with pytest.raises(ValueError, match="request must have a model id"):
        connected_client.generate_text("", "What does foobar mean?")


def test_generate_text_stream(connected_client):
    results = connected_client.generate_text_stream(
        "flan-t5-small-caikit", "What is the meaning of life?"
    )
    assert len(results) == 9


def test_generate_text_stream_with_optional_args(connected_client):
    results = connected_client.generate_text_stream(
        "flan-t5-small-caikit",
        "What is the meaning of life?",
        preserve_input_text=False,
        max_new_tokens=20,
        min_new_tokens=4,
    )
    assert len(results) == 9

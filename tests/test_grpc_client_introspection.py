import pytest
import alog
from caikit_nlp_client.grpc_client_introspection import GrpcCaikitNlpClientIntrospection
from caikit_nlp_client.grpc_channel import *

from caikit_nlp_client.model.text_generation import TextGenerationTask

log = alog.use_channel("UNIT_TEST")
@pytest.fixture
def connected_client():
    """Returns returns a grpc client connected to a locally running server"""
    config = GrpcChannelConfig(host="localhost", port=8085, insecure=True)
    return GrpcCaikitNlpClientIntrospection(make_channel(config))


def test_create_text_generation_task(connected_client):
    generated_text = connected_client.generate_text("flan-t5-small-caikit", "What does foobar mean?")
    log.debug(f"result generated text is: {generated_text}")
    assert generated_text == "a symphony of a symphony"


def test_create_text_generation_task_with_no_model_id(connected_client):
    with pytest.raises(ValueError, match="request must have a model id"):
        connected_client.generate_text("", "What does foobar mean?")


def test_create_text_generation_task_stream(connected_client):
    results = connected_client.generate_text_stream("flan-t5-small-caikit", "What is the meaning of life?")
    assert len(results) == 19
    text = ''.join(map(lambda item: item, results))
    log.debug(f"The answer to 'What is the meaning of life?` is '{text}'")

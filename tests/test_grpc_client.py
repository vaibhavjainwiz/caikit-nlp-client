import pytest
import alog
from caikit_nlp_client.grpc_client2 import GrpcCaikitNlpClient
from caikit_nlp_client.grpc_channel import *

from caikit_nlp_client.model.text_generation import TextGenerationTask

log = alog.use_channel("UNIT_TEST")
@pytest.fixture
def connected_client():
    """Returns returns a grpc client connected to a locally running server"""
    config = GrpcChannelConfig(host="localhost", port=8085, insecure=True)
    return GrpcCaikitNlpClient(make_channel(config))


def test_create_text_generation_task(connected_client):
    task_request = TextGenerationTask("What does foobar mean?")
    result = connected_client.create_text_generation_task("flan-t5-small-caikit", task_request)
    log.debug(f"result generated text is: {result.generated_text}")
    assert result.generated_text == "a symphony of a symphony"


def test_create_text_generation_task_with_no_model_id(connected_client):
    with pytest.raises(ValueError, match="request must have a model id"):
        task_request = TextGenerationTask("What does foobar mean?")
        connected_client.create_text_generation_task("", task_request)


def test_create_text_generation_task_stream(connected_client):
    task_request = TextGenerationTask("What is the meaning of life?")
    results = connected_client.create_text_generation_task_stream("flan-t5-small-caikit", task_request)
    assert len(results) == 14
    text = ''.join(map(lambda item: item.generated_text, results))
    log.debug(f"The answer to '{task_request.text}` is '{text}'")

import pytest
import grpc
import logging

from caikit_nlp_client.grpc_client.grpcclient_builder import GRPCClientBuilder

from caikit_nlp_client.model.text_generation import TextGenerationTask

@pytest.fixture
def connected_client():
    """Returns returns a grpc client connected to a running server"""
    return GRPCClientBuilder().\
        set_grpc_address("localhost").\
        set_grpc_port("8080").\
        build()


def test_create_text_generation_task(connected_client):
    task_request = TextGenerationTask("flan-t5-small-caikit", "What does foobar mean?")
    result = connected_client.create_text_generation_task(task_request)
    logging.debug(f"result generated text is: {result.generated_text}")
    assert result.generated_text == "a symphony of a symphony"


def test_create_text_generation_task_with_no_model_id(connected_client):
    with pytest.raises(ValueError, match="request must have a model id"):
        task_request = TextGenerationTask("", "What does foobar mean?")
        connected_client.create_text_generation_task(task_request)

import pytest
from caikit_nlp_client.grpc_client import GrpcCaikitNlpClient
from caikit_nlp_client.model.text_generation import TextGenerationTask


@pytest.fixture
def connected_client():
    '''Returns returns a grpc client connected to a running server'''
    return GrpcCaikitNlpClient()


def test_create_text_generation_task(connected_client):
    task_request = TextGenerationTask("foobar", "What does foobar mean?")
    connected_client.create_text_generation_task(task_request)

def test_create_text_generation_task_with_no_model_id(connected_client):
    task_request = TextGenerationTask("", "What does foobar mean?")
    connected_client.create_text_generation_task(task_request)

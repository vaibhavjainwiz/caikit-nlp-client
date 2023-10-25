import caikit_nlp_client.grpc_client as GrpcClient
import pytest

@pytest.fixture
def connected_client():
    '''Returns returns a grpc client connected to a running server'''
    return GrpcClient()
def test_CreateTextGenerationTask(connected_client):

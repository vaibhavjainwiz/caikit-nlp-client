import logging

import grpc

from caikit_nlp_client.generated.caikit.runtime.Nlp.textgenerationtaskrequest_pb2 import TextGenerationTaskRequest
from caikit_nlp_client.generated.nlpservice_pb2_grpc import NlpServiceStub

from caikit_nlp_client.client import CaikitNlpClient
from caikit_nlp_client.client_utils import prepare_certs
from caikit_nlp_client.model.text_generation import TextGenerationTask, TextGenerationTaskResult


class GRPCClient(CaikitNlpClient):
    """Client specification class"""

    def __init__(self, http_address: str, http_port: int, tls: bool, mtls: bool, server_crt: str, client_crt: str, client_key: str) -> None:
        self.client_key = client_key
        self.client_crt = client_crt
        self.server_crt = server_crt
        self.tls = tls
        self.mtls = mtls
        self.http_port = http_port
        self.http_address = http_address

    def create_text_generation_task(self, task: TextGenerationTask) -> TextGenerationTaskResult:
        logging.info("Calling CreateTextGenerationTask")




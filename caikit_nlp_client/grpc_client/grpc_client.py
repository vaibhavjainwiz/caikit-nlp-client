import logging

import grpc

from caikit_nlp_client.generated.caikit.runtime.Nlp.textgenerationtaskrequest_pb2 import TextGenerationTaskRequest
from caikit_nlp_client.generated.nlpservice_pb2_grpc import NlpServiceStub

from caikit_nlp_client.client import CaikitNlpClient
from caikit_nlp_client.client_utils import prepare_certs
from caikit_nlp_client.model.text_generation import TextGenerationTask, TextGenerationTaskResult


class GRPCClient(CaikitNlpClient):
    """Client specification class"""

    def __init__(self, grpc_address: str, grpc_port: int, tls: bool, server_crt: str, client_crt: str, client_key: str) -> None:
        self.client_key = client_key
        self.client_crt = client_crt
        self.server_crt = server_crt
        self.tls = tls
        self.grpc_port = grpc_port
        self.grpc_address = grpc_address
        self.stub = self.create_stub()

    def create_text_generation_task(self, task: TextGenerationTask) -> TextGenerationTaskResult:
        logging.info("Calling CreateTextGenerationTask")
        try:
            if task.model_id == "":
                raise ValueError("request must have a model id")

            metadata = [("mm-model-id", task.model_id)]

            request = TextGenerationTaskRequest()
            request.text = task.text
            request.preserve_input_text = False
            request.max_new_tokens = 200
            request.min_new_tokens = 10

            response = self.stub.TextGenerationTaskPredict(request=request, metadata=metadata)
            logging.debug(f"Response response: {response}")
            result = TextGenerationTaskResult(response.generated_text)
            return result
        except Exception as exc:
            logging.error(f"Caught exception {exc}, rethrowing")
            raise exc

    def create_stub(self):
        address = "{}:{}".format(self.grpc_address, self.grpc_port)
        if self.tls:
            server_ca_cert, client_key, client_cert = prepare_certs(server_cert=self.server_crt,
                                                                    client_key=self.client_key,
                                                                    client_ca=self.client_crt)
            creds = grpc.ssl_channel_credentials(root_certificates=server_ca_cert,
                                                 private_key=client_key, certificate_chain=client_cert)
            channel = grpc.secure_channel(address, creds)
        else:
            channel = grpc.insecure_channel(address)
        return NlpServiceStub(channel)

import grpc
import logging

from .client import CaikitNlpClient
from .model.text_generation import TextGenerationTask, TextGenerationTaskResult
from .generated.nlpservice_pb2_grpc import NlpServiceStub
from .generated.caikit.runtime.Nlp.textgenerationtaskrequest_pb2 import TextGenerationTaskRequest
from .generated.caikit.runtime.Nlp.serverstreamingtextgenerationtaskrequest_pb2 import ServerStreamingTextGenerationTaskRequest


class GrpcCaikitNlpClient(CaikitNlpClient):

    def __init__(self, channel: grpc.Channel) -> None:
        self.stub = NlpServiceStub(channel)

    def create_text_generation_task(self, model_id: str, task: TextGenerationTask) -> TextGenerationTaskResult:
        logging.info("Calling create_text_generation_task")
        try:
            if model_id == "":
                raise ValueError("request must have a model id")

            metadata = [("mm-model-id", model_id)]

            request = TextGenerationTaskRequest()
            request.text = task.text
            request.preserve_input_text = task.preserve_input_text
            request.max_new_tokens = task.max_new_tokens
            request.min_new_tokens = task.min_new_tokens

            response = self.stub.TextGenerationTaskPredict(request=request, metadata=metadata)
            logging.debug(f"Response: {response}")
            result = TextGenerationTaskResult(response.generated_text)
            logging.info("Calling create_text_generation_task success")
            return result
        except Exception as exc:
            logging.error(f"Caught exception {exc}, rethrowing")
            raise exc

    def create_text_generation_task_stream(self, model_id: str, task: TextGenerationTask) -> \
            [TextGenerationTaskResult]:
        logging.info("Calling create_text_generation_task_stream")
        try:
            if model_id == "":
                raise ValueError("request must have a model id")

            metadata = [("mm-model-id", model_id)]

            request = ServerStreamingTextGenerationTaskRequest()
            request.text = task.text
            request.preserve_input_text = task.preserve_input_text
            request.max_new_tokens = task.max_new_tokens
            request.min_new_tokens = task.min_new_tokens
            result = []
            for item in self.stub.ServerStreamingTextGenerationTaskPredict(metadata=metadata, request=request):
                logging.debug(f"Response item: {item}")
                resulting_item = TextGenerationTaskResult(item.generated_text)
                result.append(resulting_item)
            return result
        except Exception as exc:
            logging.error(f"Caught exception {exc}, rethrowing")
            raise exc


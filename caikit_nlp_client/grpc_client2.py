import grpc
import alog

from .client import CaikitNlpClient
from .model.text_generation import TextGenerationTask, TextGenerationTaskResult
from .generated.nlpservice_pb2_grpc import NlpServiceStub
from .generated.caikit.runtime.Nlp.textgenerationtaskrequest_pb2 import (
    TextGenerationTaskRequest,
)
from .generated.caikit.runtime.Nlp.serverstreamingtextgenerationtaskrequest_pb2 import (
    ServerStreamingTextGenerationTaskRequest,
)

log = alog.use_channel("GRPC_CLIENT")


class GrpcCaikitNlpClient(CaikitNlpClient):
    def __init__(self, channel: grpc.Channel) -> None:
        self.stub = NlpServiceStub(channel)

    def create_text_generation_task(
        self, model_id: str, task: TextGenerationTask
    ) -> TextGenerationTaskResult:
        log.info(f"Calling create_text_generation_task for {model_id}")
        try:
            if model_id == "":
                raise ValueError("request must have a model id")

            metadata = [("mm-model-id", model_id)]

            request = TextGenerationTaskRequest()
            request.text = task.text
            request.preserve_input_text = task.preserve_input_text
            request.max_new_tokens = task.max_new_tokens
            request.min_new_tokens = task.min_new_tokens

            response = self.stub.TextGenerationTaskPredict(
                request=request, metadata=metadata
            )
            log.debug(f"Response: {response}")
            result = TextGenerationTaskResult(response.generated_text)
            log.info("Calling create_text_generation_task was successful")
            return result
        except Exception as exc:
            log.error(f"Caught exception {exc}, rethrowing")
            raise exc

    def create_text_generation_task_stream(
        self, model_id: str, task: TextGenerationTask
    ) -> [TextGenerationTaskResult]:
        log.info(f"Calling create_text_generation_task_stream for {model_id}")
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
            for item in self.stub.ServerStreamingTextGenerationTaskPredict(
                metadata=metadata, request=request
            ):
                resulting_item = TextGenerationTaskResult(item.generated_text)
                result.append(resulting_item)
            log.debug(f"There are '{len(result)}' items in results")
            return result
        except Exception as exc:
            log.error(f"Caught exception {exc}, rethrowing")
            raise exc

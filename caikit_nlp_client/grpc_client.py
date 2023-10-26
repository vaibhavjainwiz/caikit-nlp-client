#import alog
from .client import CaikitNlpClient
from .model.text_generation import TextGenerationTask, TextGenerationTaskResult

#print(alog.__file__)
#log = alog.use_channel("GRPC_CLIENT")


class GrpcCaikitNlpClient(CaikitNlpClient):

    def create_text_generation_task(self, request: TextGenerationTask) -> TextGenerationTaskResult:
        #log.Info("Calling CreateTextGenerationTask")
        if request.model_id == "":
            raise ValueError ("request must have a moodel id")
        result = TextGenerationTaskResult("Random text")
        return result

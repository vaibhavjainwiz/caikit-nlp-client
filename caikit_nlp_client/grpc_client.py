import client
import model
import alog

log = alog.use_channel("GRPC_CLIENT")


class GrpcCaikitNlpClient(client.CaikitNlpClient):

    def CreateTextGenerationTask(self, request: model.TextGenerationTask) -> model.TextGenerationTaskResul:
        log.Info("Calling CreateTextGenerationTask")
        result = model.TextGenerationTaskResul()
        return result

import abc
import model


class CaikitNlpClient(abc.ABC):
    @abc.abstractmethod
    def CreateTextGenerationTask(self, request: model.TextGenerationTask) -> model.TextGenerationTaskResul:
        pass

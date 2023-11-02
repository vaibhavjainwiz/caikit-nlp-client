import abc

from .model.text_generation import TextGenerationTask, TextGenerationTaskResult


class CaikitNlpClient(abc.ABC):
    @abc.abstractmethod
    def create_text_generation_task(
        self, model_id: str, request: TextGenerationTask
    ) -> TextGenerationTaskResult:
        pass

    @abc.abstractmethod
    def create_text_generation_task_stream(
        self, model_id: str, request: TextGenerationTask
    ) -> [TextGenerationTaskResult]:
        pass

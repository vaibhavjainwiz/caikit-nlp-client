import grpc
import alog

import grpc
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from google.protobuf.descriptor_pool import DescriptorPool
from google.protobuf.message_factory import GetMessageClass

log = alog.use_channel("GRPC_CLIENT_INTROSPECTION")

class GrpcCaikitNlpClientIntrospection():

    def __init__(self, channel: grpc.Channel) -> None:
        try:
            self.reflection_db = ProtoReflectionDescriptorDatabase(channel)
            self.desc_pool = DescriptorPool(self.reflection_db)
            self.text_generation_task_request= GetMessageClass(self.desc_pool.FindMessageTypeByName('caikit.runtime.Nlp.TextGenerationTaskRequest'))
            self.server_streaming_text_generation_task_request = GetMessageClass(self.desc_pool.FindMessageTypeByName('caikit.runtime.Nlp.ServerStreamingTextGenerationTaskRequest'))
            self.generated_text_result = GetMessageClass(self.desc_pool.FindMessageTypeByName('caikit_data_model.nlp.GeneratedTextResult'))
            self.text_generation_task_predict = channel.unary_unary(
                    '/caikit.runtime.Nlp.NlpService/TextGenerationTaskPredict',
                    request_serializer=self.text_generation_task_request.SerializeToString,
                    response_deserializer=self.generated_text_result.FromString,
                    )
            self.server_streaming_text_generation_task_predict = channel.unary_stream(
                    '/caikit.runtime.Nlp.NlpService/ServerStreamingTextGenerationTaskPredict',
                    request_serializer=self.server_streaming_text_generation_task_request.SerializeToString,
                    response_deserializer=self.generated_text_result.FromString,
                    )
        except Exception as exc:
            log.error(f"Caught exception {exc}, re-throwing")
            raise exc

    def generate_text(self, model_id: str, text:str,  **kwargs) -> str:
        if model_id == "":
            raise ValueError("request must have a model id")
        try:
            log.info(f"Calling generate_text for '{model_id}'")
            metadata = [("mm-model-id", model_id)]

            request = self.text_generation_task_request()
            request.text = text
            
            request.preserve_input_text = kwargs.get("preserve_input_text", False)
            request.max_new_tokens = kwargs.get("max_new_tokens", 200)
            request.min_new_tokens = kwargs.get("min_new_tokens", 15)

            response = self.text_generation_task_predict(request=request, metadata=metadata)
            log.debug(f"Response: {response}")
            result = response.generated_text
            log.info("Calling generate_text was successful")
            return result
        except Exception as exc:
            log.error(f"Caught exception {exc}, re-throwing")
            raise exc

    def generate_text_stream(self, model_id: str, text: str,  **kwargs) -> [str]:
        if model_id == "":
            raise ValueError("request must have a model id")
        try:
            log.info(f"Calling generate_text_stream for '{model_id}'")

            metadata = [("mm-model-id", model_id)]

            request = self.server_streaming_text_generation_task_request()
            request.text = text            
            request.preserve_input_text = kwargs.get("preserve_input_text", False)
            request.max_new_tokens = kwargs.get("max_new_tokens", 200)
            request.min_new_tokens = kwargs.get("min_new_tokens", 15)
            result = []
            for item in self.server_streaming_text_generation_task_predict(metadata=metadata, request=request):
                result.append(item.generated_text)
            log.info(f"Calling generate_text_stream was successful, '{len(result)}' items in result")
            return result
        except Exception as exc:
            log.error(f"Caught exception {exc}, re-throwing")
            raise exc



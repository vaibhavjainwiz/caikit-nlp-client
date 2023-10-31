""" caikit-nlp grpc introspection

based on https://github.com/rh-aiservices-bu/llm-on-openshift/blob/main/examples/notebooks/caikit-basic-query/caikit_grpc_query_example.ipynb
"""
import grpc
from google.protobuf.descriptor_pool import DescriptorPool
from google.protobuf.message_factory import GetMessageClass
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import (
    ProtoReflectionDescriptorDatabase,
)


class CaikitTgisTextGeneration:
    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.reflection_db = ProtoReflectionDescriptorDatabase(channel)
        self.desc_pool = DescriptorPool(self.reflection_db)
        self.TextGenerationTaskRequest = GetMessageClass(
            self.desc_pool.FindMessageTypeByName(
                "caikit.runtime.Nlp.TextGenerationTaskRequest"
            )
        )()
        self.GeneratedTextResult = GetMessageClass(
            self.desc_pool.FindMessageTypeByName(
                "caikit_data_model.nlp.GeneratedTextResult"
            )
        )()
        self.TextGenerationTaskPredict = channel.unary_unary(
            "/caikit.runtime.Nlp.NlpService/TextGenerationTaskPredict",
            request_serializer=self.TextGenerationTaskRequest.SerializeToString,
            response_deserializer=self.GeneratedTextResult.FromString,
        )
        self.ServerStreamingTextGenerationTaskPredict = channel.unary_stream(
            "/caikit.runtime.Nlp.NlpService/ServerStreamingTextGenerationTaskPredict",
            request_serializer=self.TextGenerationTaskRequest.SerializeToString,
            response_deserializer=self.GeneratedTextResult.FromString,
        )

    def predict_text(self, text: str) -> dict:
        # Let's query the model!
        model_id = "flan-t5-small-caikit"
        metadata = [("mm-model-id", model_id)]

        request = self.TextGenerationTaskRequest
        request.text = "How do you bake a cake?"
        request.preserve_input_text = False
        request.max_new_tokens = 200
        request.min_new_tokens = 10

        response = self.TextGenerationTaskPredict(request=request, metadata=metadata)
        print(response.generated_text)

        return response

    def list_available_services(self):
        nlp_service = self.desc_pool.FindServiceByName("caikit.runtime.Nlp.NlpService")
        print("Available methods:")
        for m in nlp_service.methods:
            print(m.name)


if __name__ == "__main__":
    hosts = [
        # spin up a server with:
        #    RUNTIME_LIBRARY=caikit_nlp CONFIG_FILES=${caikit_config} python -m caikit.runtime
        "localhost:8080",
    ]

    for host in hosts:
        channel = grpc.insecure_channel(host)
        caikit_client = CaikitTgisTextGeneration(channel)
        response = caikit_client.predict_text("What is the temperature of the sun?")

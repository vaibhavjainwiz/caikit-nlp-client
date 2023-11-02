import argparse

from caikit_nlp_client.grpc_client.grpcclient_builder import GRPCClientBuilder
from caikit_nlp_client.model.text_generation import TextGenerationTask


parser = argparse.ArgumentParser(
    description="Client library for Caikit-TGIS to call prediction"
)

parser.add_argument(
    "--input_text", required=True, help="Input text on which prediction needs to be run"
)
parser.add_argument(
    "--grpc_address",
    required=False,
    default="localhost",
    help="Specify url to grpc service. default:localhost",
)
parser.add_argument(
    "--grpc_port",
    required=False,
    default=8085,
    help="Specify port to grpc service. default: 8085",
)
parser.add_argument(
    "--model_id", required=True, default="face-detection", help="Specify the model name"
)
parser.add_argument(
    "--tls",
    default=False,
    action="store_true",
    help="use TLS communication with gRPC endpoint",
)
parser.add_argument("--server_cert", required=False, help="Path to server certificate")
parser.add_argument("--client_cert", required=False, help="Path to client certificate")
parser.add_argument("--client_key", required=False, help="Path to client key")
args = vars(parser.parse_args())

grpc_client = (
    GRPCClientBuilder()
    .set_grpc_address(args["grpc_address"])
    .set_grpc_port(args["grpc_port"])
    .is_tls(args.get("tls"))
    .set_server_crt(args["server_cert"])
    .set_client_crt(args["client_cert"])
    .set_client_key(args["client_key"])
    .build()
)
task_request = TextGenerationTask(args["model_id"], args["input_text"])
result = grpc_client.create_text_generation_task(task_request)
print("result generated text is: ", result.generated_text)

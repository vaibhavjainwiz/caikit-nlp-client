from caikit_nlp_client.grpc_client.grpc_client import GRPCClient


class GRPCClientBuilder:
    def __init__(self):
        self.client_key = None
        self.client_crt = None
        self.server_crt = None
        self.tls = None
        self.grpc_port = None
        self.grpc_address = None

    def set_grpc_address(self, grpc_address: str):
        self.grpc_address = grpc_address
        return self

    def set_grpc_port(self, grpc_port: int):
        self.grpc_port = grpc_port
        return self

    def is_tls(self, tls: bool):
        self.tls = tls
        return self

    def set_server_crt(self, server_crt: str):
        self.server_crt = server_crt
        return self

    def set_client_crt(self, client_crt: str):
        self.client_crt = client_crt
        return self

    def set_client_key(self, client_key: str):
        self.client_key = client_key
        return self

    def build(self) -> GRPCClient:
        """GRPC client"""
        return GRPCClient(
            grpc_address=self.grpc_address,
            grpc_port=self.grpc_port,
            tls=self.tls,
            client_crt=self.client_crt,
            server_crt=self.server_crt,
            client_key=self.client_key,
        )

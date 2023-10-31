from typing import Any

from caikit_nlp_client.http_client.http_client import httpClient


class HTTPClientBuilder:

    def __init__(self):
        self.client_key = None
        self.client_crt = None
        self.server_crt = None
        self.tls = None
        self.mtls = None
        self.http_port = None
        self.http_address = None

    def set_http_address(self, http_address: str):
        self.http_address = http_address
        return self

    def set_http_port(self, http_port: int):
        self.http_port = http_port
        return self

    def is_tls(self, tls: bool):
        self.tls = tls
        return self

    def is_mtls(self, mtls: bool):
        self.mtls = mtls
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

    def build(self) -> httpClient:
        """http client"""
        return httpClient(
            http_address=self.http_address,
            http_port=self.http_port,
            tls=self.tls,
            client_crt=self.client_crt,
            server_crt=self.server_crt,
            client_key=self.client_key
        )

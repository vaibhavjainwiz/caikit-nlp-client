from dataclasses import dataclass


@dataclass
class HTTPConfig:
    host: str
    port: int
    tls: bool = False
    mtls: bool = False
    client_key = None
    client_crt = None
    server_crt = None

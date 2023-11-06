from dataclasses import dataclass


@dataclass
class HTTPConfig:
    host: str
    port: int
    tls: bool = False
    mtls: bool = False
    client_key: str = None
    client_crt: str = None
    server_crt: str = None

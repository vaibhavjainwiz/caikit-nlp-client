from dataclasses import dataclass


@dataclass
class HTTPConfig:
    host: str
    port: int
    tls: bool = False
    mTls: bool = False
    client_key = None
    client_crt = None
    server_crt = None

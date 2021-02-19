from dataclasses import dataclass


@dataclass
class IMQProtocol:
    data: str
    sourceURL: str
    destinationURL: str
    dataFormat: str = "json"
    version: str = "5.0"

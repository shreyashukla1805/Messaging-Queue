from dataclasses import dataclass
from IMQProtocol import *


@dataclass
class Request(IMQProtocol):
    requestType: str = "POST"

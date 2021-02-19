from dataclasses import dataclass
from IMQProtocol import *


@dataclass
class Response(IMQProtocol):
    status: str = "Message sent successfully"

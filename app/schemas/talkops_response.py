from pydantic import BaseModel
from typing import Any


class TalkOpsResponse(BaseModel):
    result: Any

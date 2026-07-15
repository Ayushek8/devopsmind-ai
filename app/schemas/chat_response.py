from typing import Any

from pydantic import BaseModel


class ChatResponse(BaseModel):

    success: bool

    type: str

    data: Any
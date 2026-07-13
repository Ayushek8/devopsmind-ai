from pydantic import BaseModel


class TalkOpsRequest(BaseModel):
    command: str

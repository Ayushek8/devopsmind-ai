from pydantic import BaseModel


class ExecutionCommand(BaseModel):

    domain: str

    service: str

    action: str

    parameters: dict

    requires_confirmation: bool = False

from pydantic import BaseModel
from typing import Dict


class ExecutionCommand(BaseModel):

    domain: str

    service: str

    action: str

    parameters: Dict = {}

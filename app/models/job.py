from pydantic import BaseModel


class Job(BaseModel):

    id: int

    name: str

    status: str

    conclusion: str

    html_url: str
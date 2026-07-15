from pydantic import BaseModel


class Deployment(BaseModel):

    id: int

    workflow: str

    branch: str

    status: str

    conclusion: str | None = None

    event: str | None = None

    url: str | None = None

    created_at: str | None = None

    updated_at: str | None = None
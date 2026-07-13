from fastapi import APIRouter

from app.engine.talkops_engine import TalkOpsEngine
from app.schemas.talkops_request import TalkOpsRequest
from app.schemas.talkops_response import TalkOpsResponse

router = APIRouter()

engine = TalkOpsEngine()


@router.post("/talkops", response_model=TalkOpsResponse)
def talkops(request: TalkOpsRequest):

    result = engine.execute(request.command)

    return TalkOpsResponse(
        result=result
    )

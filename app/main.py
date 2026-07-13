from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.core.config import settings

from app.schemas.review_request import ReviewRequest
from app.schemas.review_response import ReviewResponse
from app.schemas.chat_request import ChatRequest
from app.schemas.chat_response import ChatResponse

from app.services.review_service import ReviewService
from app.services.chat.chat_service import ChatService


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

review_service = ReviewService()
chat_service = ChatService()


# -------------------------------------------------
# Static Files
# -------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="app/templates"
)


# -------------------------------------------------
# Home
# -------------------------------------------------

@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# -------------------------------------------------
# Health
# -------------------------------------------------

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# -------------------------------------------------
# AI Chat Endpoint
# -------------------------------------------------

@app.post(
    "/api/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    result = chat_service.process(
        request.message
    )

    return ChatResponse(
        response=result
    )


# -------------------------------------------------
# Jenkins Review Endpoint
# -------------------------------------------------

@app.post(
    "/review/jenkinsfile",
    response_model=ReviewResponse
)
def review(request: ReviewRequest):

    result = review_service.review_jenkinsfile(
        request.content
    )

    return ReviewResponse(
        review=result
    )
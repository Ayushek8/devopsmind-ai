from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.core.config import settings

from app.schemas.chat_request import ChatRequest
from app.schemas.chat_response import ChatResponse

from app.schemas.review_request import ReviewRequest
from app.schemas.review_response import ReviewResponse

from app.services.chat.chat_service import ChatService
from app.services.review_service import ReviewService

from app.api.deployment_api import router as deployment_router
from app.api.dashboard_api import router as dashboard_router

app = FastAPI(

    title=settings.APP_NAME,

    version=settings.APP_VERSION

)

chat_service = ChatService()

review_service = ReviewService()

app.mount(

    "/static",

    StaticFiles(directory="app/static"),

    name="static"

)

templates = Jinja2Templates(

    directory="app/templates"

)

app.include_router(

    deployment_router,

    prefix="/api",

    tags=["Deployment"]

)

app.include_router(

    dashboard_router,

    prefix="/api",

    tags=["Dashboard"]

)


@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(

        request=request,

        name="index.html",

        context={}

    )


@app.get("/health")
def health():

    return {

        "status": "healthy",

        "application": settings.APP_NAME,

        "version": settings.APP_VERSION

    }


@app.post(

    "/api/chat",

    response_model=ChatResponse

)
def chat(request: ChatRequest):

    try:

        result = chat_service.process(

            request.message

        )

        if not isinstance(

            result,

            dict

        ):

            result = {

                "success": True,

                "type": "text",

                "data": result

            }

        return ChatResponse(

            **result

        )

    except Exception as e:

        print("=" * 80)

        print("CHAT ERROR")

        print("=" * 80)

        print(e)

        return ChatResponse(

            success=False,

            type="error",

            data={

                "message": str(e)

            }

        )


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
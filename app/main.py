from fastapi import FastAPI

from app.core.config import settings

from app.schemas.review_request import ReviewRequest
from app.schemas.review_response import ReviewResponse

from app.services.review_service import ReviewService

# NEW
from app.api.routes import router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# NEW
app.include_router(router)

review_service = ReviewService()


@app.get("/")
def root():
    return {
        "message": settings.APP_NAME
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/review/jenkinsfile", response_model=ReviewResponse)
def review(request: ReviewRequest):

    result = review_service.review_jenkinsfile(
        request.content
    )

    return ReviewResponse(
        review=result
    )
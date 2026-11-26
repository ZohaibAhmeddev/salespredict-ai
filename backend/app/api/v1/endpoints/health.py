from fastapi import APIRouter
from app.core.config import settings
from app.schemas.common import HealthResponse, MessageResponse

router = APIRouter(
    prefix="/health",
    tags = ["Health"]
)

@router.get("/", response_model=HealthResponse)
def health_check():
    return {
        "status": "healthy",
        'application': settings.APP_NAME,
        "version": settings.App_VERSION
    }

@router.get("/ping", response_model=MessageResponse)
def ping():
    return{
        "message":"pong"
    }

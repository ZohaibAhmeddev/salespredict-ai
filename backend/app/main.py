from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import api_router
from app.core.config import settings


app = FastAPI(
    title = settings.APP_NAME,
    description = "SalesPredict AI is a powerful tool that leverages advanced machine learning algorithms to provide accurate sales predictions for businesses. By analyzing historical sales data, market trends, and other relevant factors, SalesPredict AI helps businesses make informed decisions, optimize inventory management, and improve overall sales performance.",
    version = settings.App_VERSION,
)

#fontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# register version api routers

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def home():
    return {
        "message": "Welcome to SalesPredict AI.",
        "status": "running"
    }
from fastapi import FastAPI

app = FastAPI(
    title = "SalesPredict AI",
    description = "SalesPredict AI is a powerful tool that leverages advanced machine learning algorithms to provide accurate sales predictions for businesses. By analyzing historical sales data, market trends, and other relevant factors, SalesPredict AI helps businesses make informed decisions, optimize inventory management, and improve overall sales performance.",
    version = "1.0.0",
)

@app.get("/")
def home():
    return {
        "message": "Welcome to SalesPredict AI! Use the /docs endpoint to explore the API documentation and start making accurate sales predictions for your business.",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {
        "message": "SalesPredict AI is healthy and running smoothly.",
        "status": "healthy"
    }

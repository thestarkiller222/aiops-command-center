from fastapi import FastAPI

from backend.app.core.config import settings


app = FastAPI(
    title="AIOps Command Center",
    description="AI-powered IT Operations and Incident Management Platform",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "environment": "development",
    }
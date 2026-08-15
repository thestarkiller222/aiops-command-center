from fastapi import FastAPI

app = FastAPI(
    title="AIOps Command Center",
    description="AI-powered IT Operations and Incident Management Platform",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
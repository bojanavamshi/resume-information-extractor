from fastapi import FastAPI
from app.api.upload import router

app = FastAPI(
    title="Resume Information Extractor",
    version="1.0",
    description="Offline Resume Information Extractor using FastAPI"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Resume Information Extractor API is Running"
    }
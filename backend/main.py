from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.upload import router

app = FastAPI(
    title="Resume Information Extractor",
    version="1.0",
    description="Offline Resume Information Extractor using FastAPI"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Resume Information Extractor API is Running"
    }
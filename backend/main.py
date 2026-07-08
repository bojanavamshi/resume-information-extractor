import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.upload import router

app = FastAPI(
    title=os.getenv("API_TITLE", "Resume Information Extractor"),
    version=os.getenv("API_VERSION", "1.0.0"),
    description="Offline Resume Information Extractor using FastAPI",
)

# CORS (keep for safety during development)
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

# API routes
app.include_router(router, prefix="/api")


# ✅ IMPORTANT: Serve frontend (ONE URL FIX)
app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.get("/api")
def home():
    return {"message": "Resume Information Extractor API is Running"}
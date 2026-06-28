import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.pdf_reader import extract_text_from_pdf
from app.services.text_cleaner import clean_text
from app.services.ai_extractor import extract_resume_data
from app.services.json_formatter import format_resume_data

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

UPLOAD_FOLDER = "app/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Upload a resume PDF and extract information.
    """

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Read PDF
        text = extract_text_from_pdf(file_path)

        # Clean Text
        cleaned_text = clean_text(text)

        # Extract Information
        extracted_data = extract_resume_data(cleaned_text)

        # Convert to Resume Model
        result = format_resume_data(extracted_data)

        return {
            "status": "success",
            "data": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
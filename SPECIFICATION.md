# Resume Information Extractor - Specification

## System Overview
This project is a web-based Resume Information Extractor that extracts structured data from uploaded PDF resumes using Python backend and NLP techniques.

## Tech Stack
- Backend: Python (Flask / FastAPI)
- PDF Processing: PyMuPDF
- NLP: spaCy / Regex
- Frontend: HTML, CSS, JavaScript

## Features Implemented
- Resume PDF upload
- Text extraction from resumes
- Candidate details extraction:
  - Name
  - Email
  - Phone number
  - Skills
  - Education
  - Experience
- Data display in UI
- Export as JSON/CSV

## System Flow
Upload Resume → Extract Text → Process NLP → Extract Fields → Display Result → Export Data

## Constraints
- Only PDF files supported
- Works best with structured resumes
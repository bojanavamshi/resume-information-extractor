# User Manual

## Introduction

Resume Information Extractor helps users upload a PDF resume and receive structured candidate data through a web API.

## Requirements

- Python 3.10+
- pip
- Docker (optional)

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
```

## Running the API

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

## Uploading a Resume

Send a PDF file to the upload endpoint:

```bash
curl -X POST "http://127.0.0.1:8000/resume/upload" -F "file=@sample.pdf"
```

## Expected Output

The API returns structured data containing:

- name
- email
- phone
- skills
- education
- experience
- projects
- certifications

## Troubleshooting

### PDF not uploading

- Confirm the file is a valid PDF.
- Ensure the request uses the file field named "file".

### Empty or partial extraction

- Prefer text-based PDFs over scanned copies.
- Check whether the resume contains clearly labeled sections.

## Docker

```bash
docker build -t resume-information-extractor:latest .
docker compose up --build
```

## Security and support

- Keep your environment variables in a local .env file.
- Review SECURITY.md for vulnerability reporting guidance.


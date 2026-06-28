# Resume Information Extractor - System Specification

## Overview
The Resume Information Extractor is a web-based application that automatically extracts structured information from PDF resumes. It uses Python-based backend processing, PDF parsing, and NLP techniques to convert unstructured resume data into structured format.

## Problem Statement
Manual resume screening is time-consuming and inefficient for recruiters. This project automates the extraction of important candidate details from resumes to improve efficiency and reduce human effort.

## Objective
- Automate extraction of resume data
- Convert unstructured PDF resumes into structured data
- Reduce manual recruitment workload
- Provide downloadable structured output

## System Architecture
User uploads resume → Backend processes PDF → Text extracted using PyMuPDF/OCR → NLP/Regex processes text → Structured data generated → Displayed on frontend → Exported as JSON/CSV

## Functional Requirements

### 1. Resume Upload
- User can upload PDF resume files
- System validates file type and size

### 2. Text Extraction
- Extract text from PDF using PyMuPDF
- Use OCR for scanned resumes if required

### 3. Information Extraction
Extract the following fields:
- Full Name
- Email Address
- Phone Number
- Skills
- Education
- Work Experience
- Projects
- Certifications
- Languages
- LinkedIn Profile (if available)
- GitHub Profile (if available)

### 4. Data Processing
- Clean extracted text
- Apply regex/NLP to identify structured fields

### 5. Display Output
- Show extracted information in UI
- Allow user to review results

### 6. Export Feature
- Export data as JSON format
- Export data as CSV format

## Non-Functional Requirements
- Fast processing of resumes
- Scalable architecture
- Secure file handling
- User-friendly interface
- Accurate data extraction

## Technologies Used
### Backend
- Python
- Flask / FastAPI
- PyMuPDF
- spaCy / Regex
- OCR (Tesseract if used)

### Frontend
- HTML
- CSS
- JavaScript

## Input
- PDF Resume file

## Output
- Structured JSON/CSV data containing extracted fields

## Assumptions
- Resumes are in English
- PDF files are readable and not corrupted
- Structured resumes give better accuracy

## Limitations
- OCR accuracy may vary for scanned documents
- Unstructured resumes may reduce extraction accuracy
- Complex layouts may not be parsed perfectly

## Future Enhancements
- Machine Learning-based entity recognition
- Database storage for resumes
- Multi-format support (DOCX, images)
- Dashboard for recruiters
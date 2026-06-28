# Resume Information Extractor

## Overview

Resume Information Extractor is a web-based application that automatically extracts important information from resumes uploaded in PDF format. The system reduces manual effort by identifying and organizing candidate details into structured data.

## Features

* Upload resumes in PDF format
* Extract candidate name
* Extract email address
* Extract phone number
* Extract educational qualifications
* Extract technical skills
* Extract work experience
* Display extracted information in a user-friendly interface
* Fast and accurate resume parsing

## Technologies Used

### Backend

* Python
* Flask
* PyMuPDF (fitz)
* Regular Expressions (Regex)

### Frontend

* HTML5
* CSS3
* JavaScript

## Project Structure

```
Resume information extractor/
│
├── backend/
│   ├── app.py
│   ├── extractor.py
│   ├── requirements.txt
│   └── uploads/
│
├── README.md
├── CONTRIBUTING.md
├── USER_MANUAL.md
└── AGENTS.md
```

## Installation

1. Clone the repository.

```bash
git clone https://code.swecha.org/vamshi_22/resume-information-extractor.git
```

2. Navigate to the project folder.

```bash
cd resume-information-extractor
```

3. Create a virtual environment.

```bash
python -m venv venv
```

4. Activate the virtual environment.

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

5. Install dependencies.

```bash
pip install -r backend/requirements.txt
```

6. Run the application.

```bash
python backend/app.py
```

## Usage

1. Open the application in your browser.
2. Upload a resume in PDF format.
3. Click the Extract button.
4. View the extracted information.

## Future Enhancements

* Support DOCX resumes
* OCR support for scanned resumes
* AI-based skill extraction
* Resume ranking
* Candidate database integration

## Author

**Vamshi Bojana**

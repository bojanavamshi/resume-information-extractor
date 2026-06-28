# User Manual

## Introduction

Resume Information Extractor allows users to upload resumes and automatically extract important candidate information.

## System Requirements

* Windows, Linux, or macOS
* Python 3.10+
* Modern web browser
* Internet connection (optional)

## Starting the Application

Activate the virtual environment.

Windows

```
venv\Scripts\activate
```

Run the application.

```
python backend/app.py
```

Open your browser and visit the URL displayed in the terminal.

## Uploading a Resume

1. Open the application.
2. Click **Choose File**.
3. Select a PDF resume.
4. Click **Extract**.

## Viewing Results

The application extracts:

* Candidate Name
* Email Address
* Phone Number
* Skills
* Education
* Experience

The extracted information is displayed on the screen.

## Troubleshooting

### PDF not uploading

* Ensure the file is a valid PDF.
* Verify file size is within the supported limit.

### No information extracted

* Check that the PDF contains selectable text.
* Scanned PDFs may require OCR support.

### Application not starting

* Verify Python is installed.
* Install dependencies using:

```
pip install -r backend/requirements.txt
```

## Best Practices

* Use text-based PDF resumes.
* Keep resumes properly formatted.
* Ensure contact information is clearly written.

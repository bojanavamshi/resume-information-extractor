# Resume Information Extractor

## 📌 Project Overview
The Resume Information Extractor is a web-based application that automatically extracts structured information from PDF resumes. It uses Python, NLP, and PDF parsing techniques to convert unstructured resume data into structured format.

This project helps recruiters save time by automating resume screening and data extraction.

---

## 🎯 Features

- Upload resume in PDF format
- Extract text from resumes using PyMuPDF
- Extract structured information such as:
  - Name
  - Email
  - Phone number
  - Skills
  - Education
  - Work Experience
  - Projects
  - Certifications
- Display extracted results in UI
- Export data as JSON and CSV
- Simple and user-friendly interface

---

## 🏗️ System Architecture

User Upload → PDF Processing → Text Extraction → NLP/Regex Processing → Structured Data → UI Display → Export

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask / FastAPI
- PyMuPDF
- spaCy / Regex
- Tesseract OCR (optional)

### Frontend
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```
Resume Information Extractor/
│
├── backend/
├── frontend/
├── specs/
├── .specify/
├── README.md
├── SPECIFICATION.md
├── PLAN.md
├── TASKS.md
```

---

## 🚀 Installation & Setup

### 1. Clone Repository
```bash
git clone https://code.swecha.org/vamshi_22/resume-information-extractor.git
cd resume-information-extractor
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Project
```bash
python app.py
```

---

## 📊 Output Example

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "skills": ["Python", "Machine Learning"],
  "education": "B.Tech Computer Science",
  "experience": "2 years"
}
```

---

## ⚠️ Limitations

- Works best with structured resumes
- OCR accuracy may vary for scanned PDFs
- Complex layouts may reduce extraction accuracy

---

## 🔮 Future Improvements

- AI-based entity recognition
- Database integration
- Multi-format support (DOCX, images)
- Recruiter dashboard
- Advanced ML model for better accuracy

---

## 👨‍💻 Author

**Vamshi Bojana**  
Resume Information Extractor Project  

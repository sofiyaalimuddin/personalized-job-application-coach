# AI Career Coach – Personalized Job Application Coach

An AI-powered career assistant that helps job seekers improve their resumes, generate personalized cover letters, and develop effective job-hunting strategies using Large Language Models (LLMs).

Built with Python, Gradio, and Google's Gemini API, this application analyzes resumes against job descriptions to provide relevant, practical, and personalized career guidance.

## 🚀 Features

### 1. AI Resume Enhancer
- Analyzes resumes against a target job description.
- Identifies matching skills and missing or underrepresented skills.
- Suggests improvements to make resume content more relevant.
- Highlights relevant projects and experience.
- Generates interview preparation questions.
- Avoids inventing qualifications, skills, or professional achievements.

### 2. Personalized Cover Letter Generator
- Generates customized cover letters based on the candidate's resume and job description.
- Incorporates the company name and target job title.
- Highlights relevant skills, projects, and experience.
- Produces professional, concise, and role-specific content.

### 3. AI Career Advisor
- Evaluates the candidate's profile against a job description.
- Identifies skill gaps and areas for improvement.
- Recommends relevant career development opportunities.
- Creates a personalized learning roadmap.
- Provides interview preparation guidance.
- Suggests practical job application strategies.

### 4. Multiple Resume File Formats
Supports different resume formats:

| Format | Processing Method |
|---|---|
| PDF | PyPDF |
| Scanned/Image-based PDF | Tesseract OCR |
| DOCX | Python-docx |
| TXT | Python file handling |

OCR support allows the application to extract text from scanned PDF documents and image-based resumes.

## 📸 Application Screenshots

### Main Application
The main interface provides access to all three AI-powered career assistance tools.

![Main Application](Screenshots/main-page.png)

### AI Resume Enhancer
Analyzes resumes against job descriptions and provides personalized improvement suggestions.

![Resume Enhancer](Screenshots/resume-enhancer.png)

### Cover Letter Generator
Generates personalized cover letters using candidate information and job requirements.

![Cover Letter Generator](Screenshots/cover-letter-generator.png)

### AI Career Advisor
Provides skill gap analysis, career recommendations, learning roadmaps, and interview preparation guidance.

![Career Advisor](Screenshots/career-advisor.png)

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| User Interface | Gradio |
| Large Language Model | Google Gemini |
| LLM Integration | Google Gen AI SDK |
| PDF Processing | PyPDF, PyMuPDF |
| OCR | Tesseract, Pytesseract |
| Document Processing | Python-docx |
| Image Processing | Pillow |
| Environment Management | Python-dotenv |
| Data Processing | Pandas |

## 🏗️ Project Architecture

The application follows a modular architecture:

```text
User
  |
  v
Gradio Web Interface
  |
  v
Resume Document Parser
  |
  +---- PDF Extraction
  |
  +---- DOCX Extraction
  |
  +---- TXT Extraction
  |
  +---- OCR for Scanned PDFs
  |
  v
Extracted Resume Text + Job Description
  |
  v
AI Processing Modules
  |
  +---- Resume Enhancer
  |
  +---- Cover Letter Generator
  |
  +---- Career Advisor
  |
  v
Google Gemini API
  |
  v
Personalized AI-Generated Results
  |
  v
Gradio Interface
```

## 📂 Project Structure

```text
Personalized-Job-Application-Coach/
│
├── app.py
├── config.py
│
├── modules/
│   ├── __init__.py
│   ├── resume_enhancer.py
│   ├── cover_letter.py
│   └── career_advisor.py
│
├── utils/
│   ├── __init__.py
│   └── document_parser.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Personalized-Job-Application-Coach
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**
```powershell
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

Add your Gemini API key and Tesseract executable path:

```env
GEMINI_API_KEY=your_gemini_api_key
TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe
```

Get your Gemini API key through Google AI Studio.

### 5. Install Tesseract OCR

Tesseract is required for extracting text from scanned or image-based PDF resumes.

Install Tesseract OCR separately on your system.

The Python package `pytesseract` acts as an interface to the Tesseract OCR engine; installing the Python package alone does not install the OCR application.

If Tesseract is installed in a different location, update `TESSERACT_CMD` in your `.env` file accordingly.

### 6. Run the Application

```bash
python app.py
```

Open the local Gradio URL displayed in your terminal to access the application.

## 🔐 Security

- API credentials are stored in environment variables.
- The `.env` file is excluded from version control.
- `.env.example` provides the required configuration format without exposing private credentials.

## 🎯 Project Objective

This project explores how Large Language Models can be integrated into practical applications to solve real-world career development problems.

It combines document processing, prompt engineering, LLM integration, and interactive web application development to create an AI-powered job application assistant.

## 👩‍💻 Developer

**Sofiya**

BCA Graduate | Python | AI & Automation

GitHub: https://github.com/sofiyaalimuddin

---

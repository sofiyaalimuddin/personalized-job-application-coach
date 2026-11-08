import os
import shutil

from pathlib import Path
from pypdf import PdfReader
from docx import Document
from dotenv import load_dotenv

load_dotenv()


def extract_text_from_pdf(pdf_path):

    try:
        reader = PdfReader(pdf_path)

        if reader.is_encrypted:
            return "Error: The PDF is password-protected."

        extracted_text = []

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                extracted_text.append(page_text)

        resume_text = "\n\n".join(extracted_text)

        # If normal PDF extraction fails, try OCR.
        if not resume_text.strip():
            return extract_text_using_ocr(pdf_path)

        return resume_text

    except Exception as e:
        return f"Error extracting PDF text: {str(e)}"


def extract_text_using_ocr(pdf_path):

    try:
        import fitz
        import pytesseract
        from PIL import Image

        # Find Tesseract OCR installation.
        tesseract_path = os.getenv("TESSERACT_CMD")

        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path

        elif not shutil.which("tesseract"):
            return (
                "Error: This PDF appears to be image-based. "
                "OCR software (Tesseract) is not installed. "
                "Please install Tesseract OCR and try again."
            )

        pdf_document = fitz.open(pdf_path)

        extracted_text = []

        for page in pdf_document:

            pix = page.get_pixmap(dpi=200)

            image = Image.frombytes(
                "RGB",
                [pix.width, pix.height],
                pix.samples
            )

            page_text = pytesseract.image_to_string(image)

            if page_text.strip():
                extracted_text.append(page_text)

        pdf_document.close()

        resume_text = "\n\n".join(extracted_text)

        if not resume_text.strip():
            return "Error: OCR could not identify readable text in this PDF."

        return resume_text

    except Exception as e:
        return f"Error processing image-based PDF: {str(e)}"


def extract_text_from_docx(file_path):

    try:
        document = Document(file_path)

        extracted_text = [
            paragraph.text
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        ]

        # Also extract text from tables.
        for table in document.tables:

            for row in table.rows:

                row_text = [
                    cell.text.strip()
                    for cell in row.cells
                ]

                extracted_text.append(" | ".join(row_text))

        resume_text = "\n".join(extracted_text)

        if not resume_text.strip():
            return "Error: No readable text found in the DOCX file."

        return resume_text

    except Exception as e:
        return f"Error extracting DOCX text: {str(e)}"


def extract_text_from_txt(file_path):

    try:
        with open(file_path, "r", encoding="utf-8-sig", errors="replace") as file:
            resume_text = file.read()

        if not resume_text.strip():
            return "Error: The TXT file is empty."

        return resume_text

    except Exception as e:
        return f"Error reading TXT file: {str(e)}"


def extract_resume_text(file_path):

    if not file_path:
        return "Error: Please upload your resume."

    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension == ".docx":
        return extract_text_from_docx(file_path)

    elif extension == ".txt":
        return extract_text_from_txt(file_path)

    else:
        return "Error: Unsupported file format. Upload PDF, DOCX or TXT."
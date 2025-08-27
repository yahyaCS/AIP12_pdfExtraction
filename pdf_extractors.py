import time
from PyPDF2 import PdfReader
import pdfplumber
import fitz  # PyMuPDF


def pypdf_extractor(pdf_path):
    start = time.time()
    reader = PdfReader(pdf_path)

    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    end = time.time()
    return {
        "chars": len(text),
        "time": round(end - start, 3),
        "text": text
    }


def pdfplumber_extractor(pdf_path):
    start = time.time()
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    end = time.time()
    return {
        "chars": len(text),
        "time": round(end - start, 3),
        "text": text
    }


def pymupdf_extractor(pdf_path):
    start = time.time()
    text = ""
    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text() or ""

    doc.close()
    end = time.time()
    return {
        "chars": len(text),
        "time": round(end - start, 3),
        "text": text
    }

import time
import pypdf
import pdfplumber
import fitz  # PyMuPDF


def pypdf_extractor(pdf_path):
    start = time.time()
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = "".join([page.extract_text() or "" for page in reader.pages])
        return {"chars": len(text), "time": round(time.time() - start, 3)}
    except Exception as e:
        return {"chars": f"error: {e}", "time": round(time.time() - start, 3)}

def pdfplumber_extractor(pdf_path):
    start = time.time()
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = "".join([page.extract_text() or "" for page in pdf.pages])
        return {"chars": len(text), "time": round(time.time() - start, 3)}
    except Exception as e:
        return {"chars": f"error: {e}", "time": round(time.time() - start, 3)}

def pymupdf_extractor(pdf_path):
    start = time.time()
    try:
        doc = fitz.open(pdf_path)
        text = "".join([page.get_text() for page in doc])
        return {"chars": len(text), "time": round(time.time() - start, 3)}
    except Exception as e:
        return {"chars": f"error: {e}", "time": round(time.time() - start, 3)}


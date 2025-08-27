import time
import pypdf

def extract(pdf_path):
    start = time.time()
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = "".join([page.extract_text() or "" for page in reader.pages])
        return {"chars": len(text), "time": round(time.time() - start, 3)}
    except Exception as e:
        return {"chars": f"error: {e}", "time": round(time.time() - start, 3)}
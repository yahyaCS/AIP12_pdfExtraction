import os
import csv
import pdf_extractors as pe

EXTRACTORS = {
    "pypdf": pe.pypdf_extractor,
    "pdfplumber": pe.pdfplumber_extractor,
    "pymupdf": pe.pymupdf_extractor,
}

def evaluate_pdf(pdf_path):
    results = {}
    for name, extractor in EXTRACTORS.items():
        res = extractor(pdf_path)
        results[f"{name}_chars"] = res["chars"]
        results[f"{name}_time"] = res["time"]
    return results


def run_evaluation(pdf_folder, output_csv="results/evaluation_results.csv"):
    os.makedirs("results", exist_ok=True)
    files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    rows = []

    for file in files:
        path = os.path.join(pdf_folder, file)
        print(f"Processing: {file}")
        res = evaluate_pdf(path)
        res["file"] = file
        rows.append(res)

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["file"] + [k for r in rows for k in r.keys() if k != "file"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n Evaluation complete. Results saved to {output_csv}")
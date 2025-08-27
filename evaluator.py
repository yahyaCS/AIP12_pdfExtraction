import os
import csv
import pdf_extractors as pe

EXTRACTORS = {
    "pypdf": pe.pypdf_extractor,
    "pdfplumber": pe.pdfplumber_extractor,
    "pymupdf": pe.pymupdf_extractor,
}

def evaluate_pdf(pdf_path, file_name, text_output_dir):
    results = {}
    for name, extractor in EXTRACTORS.items():
        res = extractor(pdf_path)

        # Store metrics
        results[f"{name}_chars"] = res["chars"]
        results[f"{name}_time"] = res["time"]

        # Store extracted text (if available)
        if "text" in res:
            text_path = os.path.join(text_output_dir, f"{file_name}_{name}.txt")
            with open(text_path, "w", encoding="utf-8") as f:
                f.write(res["text"])

    return results


def run_evaluation(pdf_folder, output_csv="results/evaluation_results.csv"):
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)

    text_output_dir = os.path.join(results_dir, "text_outputs")
    os.makedirs(text_output_dir, exist_ok=True)

    files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    rows = []

    for file in files:
        path = os.path.join(pdf_folder, file)
        file_name = os.path.splitext(file)[0]
        print(f"Processing: {file}")
        res = evaluate_pdf(path, file_name, text_output_dir)
        res["file"] = file
        rows.append(res)

    output_csv_path = os.path.join(results_dir, "evaluation_results.csv")
    with open(output_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["file"] + [k for r in rows for k in r.keys() if k != "file"]
        )
        writer.writeheader()
        writer.writerows(rows)

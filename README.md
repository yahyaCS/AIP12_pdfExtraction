# 📄 PDF Extraction Evaluation

This project evaluates different open-source Python PDF extraction libraries on sample PDF files.
It measures the extraction time and number of extracted characters for comparison.

## 📂 Project Structure

| File / Folder                    | Description                                                     |
| -------------------------------- | --------------------------------------------------------------- |
| `results/`                       | Stores all results (CSV + extracted text)                       |
| `results/evaluation_results.csv` | Aggregated metrics (chars & time for each extractor per PDF)    |
| `results/text_outputs/`          | Extracted text files for each PDF and extractor                 |
| `pdf_extractors.py`              | Contains extractor functions for pypdf, pdfplumber, and pymupdf |
| `evaluator.py`                   | Runs all extractors, saves metrics, and writes extracted text   |
| `run_evaluation.py`              | Main script to execute the evaluation                           |
| `README.md`                      | Project documentation                                           |



## 📦 Dependencies

- pypdf

- pdfplumber

- PyMuPDF

## 📊 Example Output

### CSV (evaluation_results.csv)

| File        | pypdf\_chars | pypdf\_time | pdfplumber\_chars | pdfplumber\_time | pymupdf\_chars | pymupdf\_time |
| ----------- | ------------ | ----------- | ----------------- | ---------------- | -------------- | ------------- |
| sample2.pdf | 23,077       | 0.318s      | 21,986            | 1.280s           | 23,079         | 0.177s        |
| sample.pdf  | 72,593       | 0.840s      | 67,580            | 3.671s           | 51,183         | 0.204s        |
| fyp.pdf     | 137,180      | 3.905s      | 124,133           | 11.176s          | 137,257        | 0.409s        |

### Extracted Text Files (results/text_outputs/)

Each extractor writes a separate .txt file, e.g.:
```
results/text_outputs/sample2_pypdf.txt
results/text_outputs/sample2_pdfplumber.txt
results/text_outputs/sample2_pymupdf.txt
```
## 📝 Conclusion

Based on the evaluation across multiple runs on sample PDFs:

### Accuracy (Character Count):

- pypdf and pymupdf consistently produced nearly identical character counts.

- pdfplumber returned slightly fewer characters, suggesting occasional differences in text extraction fidelity.

### Performance (Speed):

- pymupdf was the fastest extractor across all files.

- pypdf performed moderately well, slower than pymupdf but still efficient.

- pdfplumber was the slowest, often taking several times longer than the other extractors.

### Overall Recommendation:

- Use pymupdf when speed is critical and character accuracy is sufficient.

- Use pypdf as a balanced option for reliable extraction.

- Use pdfplumber only when fine-grained layout or structure analysis is required, despite its slower performance.

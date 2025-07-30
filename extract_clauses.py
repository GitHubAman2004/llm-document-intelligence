import fitz  # PyMuPDF

def extract_policy_clauses(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()

    # Clean and split text into clauses
    text = text.replace('\xa0', ' ')  # remove non-breaking spaces
    lines = text.split("\n")

    # Extract clauses with sufficient length
    clauses = [line.strip() for line in lines if len(line.strip()) > 100]

    return clauses

# Test (optional)
if __name__ == "__main__":
    clauses = extract_policy_clauses("BAJHLIP23020V012223.pdf")
    print(f"✅ Extracted {len(clauses)} clauses\n")

    for i, clause in enumerate(clauses[:5]):
        print(f"Clause {i+1}:\n{clause}\n{'-'*50}")

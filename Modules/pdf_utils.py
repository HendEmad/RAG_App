from pypdf import PdfReader

# extract text from pdf
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# chunking --> divide text into chunks
def chunk_text(text, chunk_size=500):
    chunks=[]
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks
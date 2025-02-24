import fitz  # PyMuPDF


class PDFParser:
    @staticmethod
    def extract_text(pdf_path):
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
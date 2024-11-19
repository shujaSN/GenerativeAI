import fitz  # PyMuPDF

class FileLoader:

    def load_pdf(self, file_path):
        doc = fitz.open(file_path)
        text = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text += page.get_text()
        return text

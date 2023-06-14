import PyPDF2

# Passes the .pdf file and returns its version
def get_pdf_version(file_path):
    doc = PyPDF2.PdfReader(file_path)
    doc.stream.seek(0)  # Necessary since the comment is ignored for the PDF analysis
    version_code = str(doc.stream.readline())
    if version_code.__contains__("1.5"):
        return "1.5"
    elif version_code.__contains__("1.3"):
        return "1.3"

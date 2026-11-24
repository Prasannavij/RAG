import fitz
from pathlib import Path


def load_pdf(file_path):

    documents = []

    pdf = fitz.open(file_path)

    for page_number, page in enumerate(pdf):

        text = page.get_text("text")

        if text.strip():

            documents.append({
                "text": text,
                "metadata": {
                    "source": Path(file_path).name,
                    "page": page_number + 1
                }
            })

    pdf.close()

    return documents


def load_documents(folder_path):

    all_documents = []

    for file_path in Path(folder_path).glob("*.pdf"):

        documents = load_pdf(file_path)

        all_documents.extend(documents)

    return all_documents
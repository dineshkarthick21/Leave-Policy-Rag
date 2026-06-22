from langchain_community.document_loaders import PyPDFLoader

def load_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    print(f"Total Pages: {len(documents)}")

    return documents
from src.loader import load_pdf
from src.chunker import create_chunks
from src.vector_db import build_vector_db

print("Loading PDF...")

documents = load_pdf(
    "data/sample.pdf"
)

print("Creating Chunks...")

chunks = create_chunks(
    documents
)

print("Building Vector DB...")

build_vector_db(
    chunks
)

print("Vector DB Updated Successfully!")
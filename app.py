from langchain_community.vectorstores import FAISS
from src.embedder import get_embeddings
from src.llm import get_llm
from src.rag_pipeline import ask_rag

print("Loading Vector Database...")

db = FAISS.load_local(
    "vectorstore/faiss_index",
    get_embeddings(),
    allow_dangerous_deserialization=True
)

llm = get_llm()

while True:

    question = input(
        "\nAsk Question: "
    ).strip()

    if question.lower() == "exit":
        break

    if not question:
        print("Question cannot be empty.")
        continue

    answer = ask_rag(
        question,
        db,
        llm
    )

    print("\nAnswer:")
    print(answer)
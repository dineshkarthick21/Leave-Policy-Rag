from langchain_text_splitters import RecursiveCharacterTextSplitter
def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    print(f"Total Chunks: {len(chunks)}")

    return chunks
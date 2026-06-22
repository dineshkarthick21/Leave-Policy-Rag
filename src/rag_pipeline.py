from src.retriever import retrieve_chunks

def ask_rag(question, db, llm):

    docs = retrieve_chunks(
        db,
        question
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Context:
    {context}

    Question:
    {question}

    Answer based only on the context.
    """

    response = llm.invoke(
        prompt
    )

    return response.content
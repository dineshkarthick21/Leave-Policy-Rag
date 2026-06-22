def retrieve_chunks(db, question):

    results = db.similarity_search(
        question,
        k=3
    )

    return results
from embeddings.embedding_model import generate_query_embedding
from vectorstore.chroma_store import get_collection

from config.settings import TOP_K, SIMILARITY_THRESHOLD


def retrieve_documents(query, top_k=TOP_K):

    collection = get_collection()

    query_embedding = generate_query_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    retrieved_documents = []

    if not results["documents"]:
        return retrieved_documents

    for text, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):

        similarity = 1 - distance

        if similarity >= SIMILARITY_THRESHOLD:

            retrieved_documents.append({
                "text": text,
                "metadata": metadata,
                "similarity": similarity
            })

    return retrieved_documents
import ollama

from config.settings import EMBEDDING_MODEL


def generate_embeddings(texts):

    if not texts:
        return []

    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=texts
    )

    return response["embeddings"]


def generate_query_embedding(query):

    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=query
    )

    return response["embeddings"][0]
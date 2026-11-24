import chromadb
import uuid

from config.settings import CHROMA_DIR, COLLECTION_NAME


client = chromadb.PersistentClient(
    path=str(CHROMA_DIR)
)


collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    metadata={"hnsw:space": "cosine"}
)


def store_documents(chunks, embeddings):

    if len(chunks) != len(embeddings):
        raise ValueError("Chunks and embeddings count mismatch")

    if not chunks:
        return

    ids = [
        str(uuid.uuid4())
        for _ in chunks
    ]

    collection.add(
        ids=ids,

        documents=[
            item["text"]
            for item in chunks
        ],

        embeddings=embeddings,

        metadatas=[
            item["metadata"]
            for item in chunks
        ]
    )

    print(f"Stored {len(chunks)} chunks successfully")


def get_collection():

    return collection
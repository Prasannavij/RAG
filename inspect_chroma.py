from vectorstore.chroma_store import get_collection

collection = get_collection()

print("Collection Name:", collection.name)

print("Total Stored Chunks:", collection.count())

results = collection.get(
    limit=3,
    include=[
        "documents",
        "metadatas",
        "embeddings"
    ]
)

for i in range(len(results["ids"])):

    print("\n------------------------")

    print("ID:", results["ids"][i])

    print("TEXT:")
    print(results["documents"][i])

    print("METADATA:")
    print(results["metadatas"][i])

    print("EMBEDDING DIMENSION:")
    print(len(results["embeddings"][i]))

    print("FIRST 5 VECTOR VALUES:")
    print(results["embeddings"][i][:5])
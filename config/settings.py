from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DOCUMENT_DIR = BASE_DIR / "documents"
CHROMA_DIR = BASE_DIR / "chroma_db"

LLM_MODEL = "gemma3"
EMBEDDING_MODEL = "nomic-embed-text"

COLLECTION_NAME = "rag_documents"

# Chunking configuration
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Retrieval configuration
TOP_K = 5
SIMILARITY_THRESHOLD = 0.75

# LLM configuration
TEMPERATURE = 0.2
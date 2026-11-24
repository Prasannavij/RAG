from ingestion.document_loader import load_documents
from ingestion.text_splitter import create_chunks

from embeddings.embedding_model import generate_embeddings

from vectorstore.chroma_store import store_documents

from retrieval.retriever import retrieve_documents
from retrieval.reranker import DocumentReranker

from prompts.rag_prompt import create_rag_prompt

from generation.llm import generate_answer


class RAGPipeline:

    def __init__(self):

        self.reranker = DocumentReranker()

    def ingest(self, folder_path):

        print("Loading documents...")

        documents = load_documents(folder_path)

        print("Total pages:", len(documents))

        print("Creating chunks...")

        chunks = create_chunks(documents)

        print("Total chunks:", len(chunks))

        print("Generating embeddings...")

        embeddings = generate_embeddings([
            chunk["text"]
            for chunk in chunks
        ])

        print("Storing vectors...")

        store_documents(chunks, embeddings)

        print("Ingestion completed!")

    def ask(self, query):

        print("Retrieving documents...")

        retrieved = retrieve_documents(query, top_k=10)

        if not retrieved:
            return "I could not find relevant information in the documents."

        print("Reranking documents...")

        ranked = self.reranker.rerank(
            query,
            retrieved,
            top_n=3
        )

        print("Generating prompt...")

        prompt = create_rag_prompt(query, ranked)

        print("Generating answer...")

        answer = generate_answer(prompt)

        return answer
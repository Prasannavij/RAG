from sentence_transformers import CrossEncoder


class DocumentReranker:

    def __init__(
        self,
        model_name="cross-encoder/ms-marco-MiniLM-L-6-v2"
    ):

        self.model = CrossEncoder(model_name)

    def rerank(self, query, documents, top_n=3):

        if not documents:
            return []

        pairs = [
            (query, document["text"])
            for document in documents
        ]

        scores = self.model.predict(pairs)

        ranked_documents = []

        for document, score in zip(documents, scores):

            ranked_documents.append({
                **document,
                "rerank_score": float(score)
            })

        ranked_documents.sort(
            key=lambda x: x["rerank_score"],
            reverse=True
        )

        return ranked_documents[:top_n]
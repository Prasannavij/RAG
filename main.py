from pipeline.rag_pipeline import RAGPipeline

from config.settings import DOCUMENT_DIR


def main():

    rag = RAGPipeline()

    print("===== RAG DOCUMENT ASSISTANT =====")

    choice = input(
        "1. Ingest documents\n"
        "2. Ask a question\n"
        "Choose: "
    )

    if choice == "1":

        rag.ingest(str(DOCUMENT_DIR))

    elif choice == "2":

        while True:

            query = input("\nEnter your question: ")

            if query.lower() == "exit":
                break

            answer = rag.ask(query)

            print("\n===== ANSWER =====")

            print(answer)

    else:

        print("Invalid choice")


if __name__ == "__main__":
    main()
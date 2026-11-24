from config.settings import CHUNK_SIZE, CHUNK_OVERLAP


SEPARATORS = ["\n\n", "\n", ". ", " ", ""]


def split_text(text, chunk_size=CHUNK_SIZE,
               chunk_overlap=CHUNK_OVERLAP):

    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive")

    if chunk_overlap < 0 or chunk_overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size")

    text = text.strip()

    if not text:
        return []

    if len(text) <= chunk_size:
        return [text]

    # Find the best available separator
    separator = ""

    for sep in SEPARATORS:
        if sep and sep in text:
            separator = sep
            break

    if not separator:
        separator = ""

    if separator:
        parts = text.split(separator)
    else:
        parts = list(text)

    chunks = []
    current_chunk = ""

    for part in parts:

        candidate = (
            current_chunk + separator + part
            if current_chunk else part
        )

        if len(candidate) <= chunk_size:
            current_chunk = candidate

        else:

            if current_chunk:
                chunks.append(current_chunk)

            if len(part) > chunk_size:
                # Split oversized segments
                start = 0
                while start < len(part):
                    end = start + chunk_size
                    chunks.append(part[start:end])
                    start += chunk_size - chunk_overlap

                current_chunk = ""

            else:
                current_chunk = part

    if current_chunk:
        chunks.append(current_chunk)

    # Add overlap between adjacent chunks
    result = []

    for i, chunk in enumerate(chunks):

        if i == 0:
            result.append(chunk)
        else:
            previous = chunks[i - 1]
            overlap = previous[-chunk_overlap:] if chunk_overlap else ""
            result.append(overlap + chunk)

    return result


def create_chunks(documents):

    chunked_documents = []

    for document in documents:

        text_chunks = split_text(document["text"])

        for index, chunk in enumerate(text_chunks):

            chunked_documents.append({
                "text": chunk,
                "metadata": {
                    **document["metadata"],
                    "chunk_id": index
                }
            })

    return chunked_documents
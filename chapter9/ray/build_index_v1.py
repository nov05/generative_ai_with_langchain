"""Build and save FAISS index from Ray documentation."""

import ray
import numpy as np
from langchain_community.document_loaders import RecursiveUrlLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# Initialize Ray
ray.init()

# Initialize the embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")


# Create a function to preprocess documents
@ray.remote
def preprocess_documents(docs):
    print(f"Preprocessing batch of {len(docs)} documents")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(docs)
    print(f"Generated {len(chunks)} chunks")
    return chunks


# Create a function to embed chunks in parallel
@ray.remote
def embed_chunks(chunks):
    print(f"Embedding batch of {len(chunks)} chunks")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    return FAISS.from_documents(chunks, embeddings)


def build_index(base_url="https://docs.ray.io/en/master/", batch_size=50):
    # Create index directory if it doesn't exist
    os.makedirs("faiss_index", exist_ok=True)

    # Choose a more specific section for faster processing
    # You can adjust this URL to include more or less content
    print(f"Loading documentation from {base_url}")
    loader = RecursiveUrlLoader(base_url)
    docs = loader.load()
    print(f"Loaded {len(docs)} documents")

    # Preprocess in parallel with smaller batches
    chunks_futures = []
    for i in range(0, len(docs), batch_size):
        batch = docs[i : i + batch_size]
        chunks_futures.append(preprocess_documents.remote(batch))

    print("Waiting for preprocessing to complete...")
    all_chunks = []
    for chunks in ray.get(chunks_futures):
        all_chunks.extend(chunks)
    print(f"Total chunks: {len(all_chunks)}")

    # Split chunks for parallel embedding
    num_workers = 4
    chunk_batches = np.array_split(all_chunks, num_workers)

    # Embed in parallel
    print("Starting parallel embedding...")
    index_futures = [embed_chunks.remote(batch) for batch in chunk_batches]
    indices = ray.get(index_futures)

    # Merge indices
    print("Merging indices...")
    index = indices[0]
    for idx in indices[1:]:
        index.merge_from(idx)

    # Save the index
    print("Saving index...")
    index.save_local("faiss_index")
    print("Index saved to 'faiss_index' directory")

    return index


if __name__ == "__main__":
    # You can customize which part of the documentation to index
    # For faster testing, use a smaller section:
    # index = build_index("https://docs.ray.io/en/master/ray-core/")

    # For complete documentation:
    index = build_index()

    # Test the index
    print("\nTesting the index:")
    results = index.similarity_search("How can Ray help with deploying LLMs?", k=2)
    for i, doc in enumerate(results):
        print(f"\nResult {i + 1}:")
        print(f"Source: {doc.metadata.get('source', 'Unknown')}")
        print(f"Content: {doc.page_content[:150]}...")

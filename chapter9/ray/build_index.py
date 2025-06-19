"""Build and save FAISS index from Ray documentation (run once)"""

import gc
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import RecursiveUrlLoader
import numpy as np
import os

# Nov05: For limited memory environment
NUM_CPUS_INIT = 1
NUM_CPUS_PREPROCESS = 0.25
NUM_CPUS_EMBED = 1
NUM_WORKERS = 4
MINI_BATCH_SIZE = int(1e4)


# Nov05: For limited memory environment
def init_ray_env(num_cpus=NUM_CPUS_INIT):
    os.environ["RAY_memory_usage_threshold"] = "0.95"
    os.environ["RAY_DEDUP_LOGS"] = "0"
    import ray
    ray.init(num_cpus=num_cpus)
    return ray


# Initialize Ray
# ray.init()          # nov05
ray = init_ray_env()  # nov05
# Initialize the embedding model
embeddings = HuggingFaceEmbeddings(
    # https://huggingface.co/sentence-transformers/all-mpnet-base-v2
    model_name="sentence-transformers/all-mpnet-base-v2"
)


# Create a function to preprocess documents in parallel
@ray.remote(num_cpus=NUM_CPUS_PREPROCESS)
def preprocess_documents(docs):
    """
        Split documents into manageable chunks
        The @ray.remote decorator makes these functions run in separate Ray workers.
    """
    print(f"Preprocessing batch of {len(docs)} documents")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(docs)
    print(f"🟢 Generated {len(chunks)} chunks")
    return chunks


# Create a function to embed chunks in parallel
@ray.remote(num_cpus=NUM_CPUS_EMBED)
def embed_chunks(chunks):
    """
        Convert text chunks into vector embeddings and builds FAISS indices
        The @ray.remote decorator makes these functions run in separate Ray workers.
    """
    print(f"Embedding batch of {len(chunks)} chunks...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2")
    return FAISS.from_documents(chunks, embeddings)


def build_index(base_url="https://docs.ray.io/en/master/", batch_size=50):
    # Create index directory if it doesn't exist
    os.makedirs("faiss_index", exist_ok=True)

    # Choose a more specific section for faster processing
    # You can adjust this URL to include more or less content
    print(f"Loading documentation from {base_url}...")
    loader = RecursiveUrlLoader(base_url)
    docs = loader.load()
    print(f"🟢 Loaded {len(docs)} documents")

    # Preprocess in parallel with smaller batches
    chunks_futures = []
    for i in range(0, len(docs), batch_size):
        batch = docs[i: i + batch_size]
        chunks_futures.append(preprocess_documents.remote(batch))

    print("Waiting for preprocessing to complete...")
    all_chunks = []
    for chunks in ray.get(chunks_futures):
        all_chunks.extend(chunks)
    print(f"👉 Total chunks: {len(all_chunks)}")
    del docs, chunks_futures
    gc.collect()

    # Split chunks for parallel embedding
    chunk_batches = np.array_split(all_chunks, NUM_WORKERS)
    # Embed in parallel, changed by Nov05
    print("Starting parallel embedding...")
    index_futures = []
    for chunk_batch in chunk_batches:
        if MINI_BATCH_SIZE and len(chunk_batch) > MINI_BATCH_SIZE:
            # split to mini batches
            mini_batches = [
                chunk_batch[i:i+MINI_BATCH_SIZE] for i in range(0, len(chunk_batch), MINI_BATCH_SIZE)]
        else:  # no split if MINI_BATCH_SIZE is None, 0, False, or large
            mini_batches = [chunk_batch]
        index_futures.extend(
            [embed_chunks.remote(mini_batch) for mini_batch in mini_batches])
    indices = ray.get(index_futures)
    # Added by Nov05
    del index_futures
    gc.collect()

    # Merge indices
    print("Merging indices...")
    index = indices[0]
    for idx in indices[1:]:
        index.merge_from(idx)

    # Save the index
    print("Saving index...")
    index.save_local("faiss_index")
    print("🟢 Index saved to 'faiss_index' directory")

    return index


if __name__ == "__main__":

    # You can customize which part of the documentation to index
    # For faster testing, use a smaller section:
    # index = build_index("https://docs.ray.io/en/master/ray-core/")

    # For complete documentation:
    # Nov05: Reduce batch_size for dev container
    index = build_index(batch_size=20)

    # Test the index
    print("Testing the index...")
    results = index.similarity_search(
        "How can Ray help with deploying LLMs?", k=3)
    for i, doc in enumerate(results):
        print(
            f"Result {i + 1}:\n"
            f"Source: {doc.metadata.get('source', 'Unknown')}\n"
            f"Content: {doc.page_content[:150]}...\n"
        )

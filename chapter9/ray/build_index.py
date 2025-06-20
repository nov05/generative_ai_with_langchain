"""
    Build and save FAISS index from Ray documentation (run once)
"""

import gc
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import RecursiveUrlLoader
import os
import pickle


# Nov05: For limited memory environment, e.g. VS Code Dev Container
MODEL_NAME = "all-MiniLM-L6-v2"  # For GPU with small memory
INIT_NUM_CPUS = 1
INIT_NUM_GPUS = 1
PREPROCESS_BATCH_SIZE = 20  # Preprocessing batch size
PREPROCESS_NUM_CPUS = 0.25
EMBED_BATCH_SIZE = int(1e4)  # Embedding chunk batch size
EMBED_NUM_CPUS = None
EMBED_NUM_GPUS = 1


# Nov05: For limited memory environment
def init_ray_env():
    # Set before import
    os.environ["RAY_memory_usage_threshold"] = "0.95"
    os.environ["RAY_DEDUP_LOGS"] = "0"
    import ray
    # https://docs.ray.io/en/latest/ray-core/api/doc/ray.init.html
    ray.init(
        num_cpus=INIT_NUM_CPUS,
        num_gpus=INIT_NUM_GPUS,
    )
    return ray


# Initialize Ray
# ray.init()          # Nov05
ray = init_ray_env()  # Nov05


# Create a function to preprocess documents in parallel
@ray.remote(num_cpus=PREPROCESS_NUM_CPUS)
def preprocess_documents(docs):
    """
        Split documents into manageable chunks
        The @ray.remote decorator makes these functions run in separate Ray workers.
        E.g. Chunk size 500, overlap 50, the Ray documents will be split to 293040 Chunks.
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
@ray.remote(num_cpus=EMBED_NUM_CPUS, num_gpus=EMBED_NUM_GPUS)
def embed_chunks(chunks, embedder):
    """
        Convert text chunks into vector embeddings and builds FAISS indices
        The @ray.remote decorator makes these functions run in separate Ray workers.
    """
    print(f"Embedding batch of {len(chunks)} chunks...")
    # Initialize inside every worker. Each worker loads the full model into GPU memory.
    # It might cause crashes due to Out-Of-Memory or double-free in CUDA contexts.
    # https://huggingface.co/sentence-transformers/all-mpnet-base-v2
    return FAISS.from_documents(chunks, embedder)


def build_index(
    base_url="https://docs.ray.io/en/master/",
    index_dir="faiss_index",
    checkpoint_dir="cache",
    embedder=None,
):
    # Create index directory if it doesn't exist
    os.makedirs(index_dir, exist_ok=True)
    os.makedirs(checkpoint_dir, exist_ok=True)

    # Check for cached chunks first
    chunks_file = os.path.join(checkpoint_dir, "chunks.pkl")
    if os.path.exists(chunks_file):
        print("Loading cached chunks...")
        with open(chunks_file, 'rb') as f:
            chunks = pickle.load(f)
        print(f"🟢 Loaded {len(chunks)} cached chunks")
    else:
        # -----------------------------------------------------------
        # Load documents
        # -----------------------------------------------------------
        # Choose a more specific section for faster processing
        # You can adjust this URL to include more or less content
        print(f"Loading documentation from {base_url}...")
        loader = RecursiveUrlLoader(base_url)
        docs = loader.load()
        print(f"🟢 Loaded {len(docs)} documents")

        # -----------------------------------------------------------
        # Preprocess documents
        # -----------------------------------------------------------
        # Preprocess in parallel in batches
        chunk_futures = []
        for i in range(0, len(docs), PREPROCESS_BATCH_SIZE):
            batch = docs[i: i+PREPROCESS_BATCH_SIZE]
            chunk_futures.append(preprocess_documents.remote(batch))
        print("Waiting for preprocessing to complete...")
        chunks = []
        for future in ray.get(chunk_futures):
            chunks.extend(future)
        print(f"👉 Total chunks: {len(chunks)}")
        del docs, chunk_futures
        gc.collect()
        # Save chunks for future use
        print("Saving chunks in cache...")
        with open(chunks_file, 'wb') as f:
            pickle.dump(chunks, f)
        print("🟢 Chunks saved in cache")

    # Check if FAISS index already exists
    index_file = os.path.join(index_dir, "index.faiss")
    if os.path.exists(index_file):
        print(f"Loading existing FAISS index from '{index_dir}'...")
        embeddings = HuggingFaceEmbeddings(
            model_name=MODEL_NAME,
            model_kwargs={"device": "cuda"}  # GPU
        )
        index = FAISS.load_local(
            index_dir,
            embeddings,
            allow_dangerous_deserialization=True
        )
        print(f"🟢 Loaded existing index with {index.index.ntotal} vectors")
        return index
    print("No existing index found")

    # -----------------------------------------------------------
    # Embed document chunks in parallel
    # -----------------------------------------------------------
    # Create chunk batches for parallel embedding
    index_futures = []
    for i in range(0, len(chunks), EMBED_BATCH_SIZE):
        batch = chunks[i: i+EMBED_BATCH_SIZE]
        index_futures.append(embed_chunks.remote(batch, embedder))
    # Get results with progress tracking
    indices = []
    for i, future in enumerate(index_futures):
        indices.append(ray.get(future))
        print(f"🟢 Completed {i+1}/{len(index_futures)} embedding batches")
    del chunks, index_futures
    gc.collect()
    # Merge indices
    print("Merging indices...")
    index = indices[0]
    for idx in indices[1:]:
        index.merge_from(idx)
    del indices
    gc.collect()

    # -----------------------------------------------------------
    # Save the index
    # -----------------------------------------------------------
    print("Saving index...")
    index.save_local(index_dir)
    print(f"🟢 Index saved to directory {index_dir}")
    return index


if __name__ == "__main__":

    # Initialize the embedding model
    embedder = HuggingFaceEmbeddings(
        # https://huggingface.co/sentence-transformers/all-mpnet-base-v2
        # model_name="sentence-transformers/all-mpnet-base-v2",
        model_name=MODEL_NAME,           # Nov05: use a smaller model
        model_kwargs={"device": "cuda"}  # Nov05: GPU
    )
    # You can customize which part of the documentation to index
    # For faster testing, use a smaller section:
    # index = build_index(base_url="https://docs.ray.io/en/master/ray-core/")
    # For complete documentation:
    # index = build_index()
    index = build_index(
        base_url="https://docs.ray.io/en/master/ray-core/",
        embedder=embedder,
    )

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

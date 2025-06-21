"""
    Ray Server with pre-built FAISS index
    Loads the index and serves the search API (runs continuously)
"""

from fastapi import FastAPI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from ray import serve
import time

# MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
# https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
MODEL_NAME = "all-MiniLM-L6-v2"  # For GPU with small memory, e.g. 4GB
INDEX_DIR = "faiss_index"
INIT_NUM_CPUS = 1
INIT_NUM_GPUS = None

# Initialize Ray
# ray.init()
# Define our FastAPI app
# app = FastAPI()


@serve.deployment
class SearchDeployment:
    def __init__(self,
                 index_dir=INDEX_DIR):
        print("Loading pre-built index...")
        # Initialize the embedding model - must match what was used for building
        self.embeddings = HuggingFaceEmbeddings(
            model_name=MODEL_NAME,
            model_kwargs={"device": "cpu"}
        )
        # Check if index directory exists
        import os
        if not os.path.exists("faiss_index") or not os.path.isdir(index_dir):
            error_msg = """
⚠️  ERROR: FAISS index directory not found!

To build the index, please run:
    $ python build_index.py

This will crawl the Ray documentation, create embeddings, and save the index
to the 'faiss_index' directory. Once the index is built, you can restart this service.
"""
            print(error_msg)
            raise FileNotFoundError(error_msg)
        # Load the pre-built index
        try:
            self.index = FAISS.load_local(
                index_dir,
                self.embeddings,
                allow_dangerous_deserialization=True,  # Nov05
            )
            print(f"🟢 Successfully loaded index")
        except Exception as e:
            error_msg = f"""
⚠️  ERROR: Failed to load FAISS index: {e}

The index directory exists but could not be loaded correctly.
This might indicate a corrupted index or version mismatch.

Please rebuild the index by running:
    $ python build_index.py
"""
            print(error_msg)
            raise RuntimeError(error_msg)
        print("🟢 SearchDeployment initialized successfully")

    async def __call__(self, request):
        query = request.query_params.get("query", "")
        if not query:
            return {
                "results": [],
                "status": "empty_query",
                "message": "Please provide a query parameter",
            }
        n_results = request.query_params.get("n_results", "")
        n_results = 2 if not n_results else int(n_results)
        try:
            # Search the index
            results = self.index.similarity_search_with_score(
                query, k=n_results)
            # Format results for response
            formatted_results = []
            for doc, score in results:
                formatted_results.append(
                    {
                        "content": doc.page_content,
                        "source": doc.metadata.get("source", "Unknown"),
                        "score": float(
                            score
                        ),  # Convert numpy float to Python float for JSON serialization
                    }
                )
            return {
                "results": formatted_results,
                "status": "success",
                "message": f"Found {len(formatted_results)} results",
            }
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            print(f"⚠️  Error during search: {e}\n{error_details}")
            return {
                "results": [],
                "status": "error",
                "message": f"⚠️  Search failed: {e}",
                "error_details": error_details,
            }


# # For testing the deployment locally
# @app.get("/search")
# async def search(query: str = ""):
#     handle = serve.get_deployment_handle("SearchDeployment")
#     return await handle.remote({"query_params": {"query": query}})


# Nov05: If you deploy in bash, comment out the main block.
'''
$ ray stop --force
$ ray start --head
$ serve deploy serve_index.yaml
'''
deployment = SearchDeployment.bind()
# if __name__ == "__main__":

#     try:
#         import ray
#         ray.init(
#             num_cpus=INIT_NUM_CPUS,
#             num_gpus=INIT_NUM_GPUS,
#             # ignore_reinit_error=True,
#         )
#         # Deploy the search service
#         deployment = SearchDeployment.bind()
#         serve.run(deployment, name="doc_search")
#         print("\n" + "=" * 60)
#         print("🟢 Service started successfully!")
#         print("-" * 60)
#         print("Service URL: http://localhost:8000/")
#         print(
#             "Example query: http://localhost:8000/?query=How%20can%20Ray%20help%20with%20deploying%20LLMs%3F"
#         )
#         print("=" * 60 + "\n")
#         # Added by Nov05: Keep the script alive for 3600s (1 hour)
#         # serve.run() alone doesn’t block.
#         while True:
#             time.sleep(3600)
#     except FileNotFoundError as e:
#         # Index not found error is already handled with a clear message
#         import sys
#         sys.exit(1)
#     except Exception as e:
#         print(
#             f"⚠️  ERROR: Failed to start service: {e}\n"
#             "If this is related to the FAISS index, please rebuild it with:"
#             "$ python build_index.py")
#         import traceback
#         traceback.print_exc()
#         import sys
#         sys.exit(1)

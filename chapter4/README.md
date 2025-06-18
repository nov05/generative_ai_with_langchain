# Chapter 4 - Building Intelligent RAG Systems

Please make sure you set up your environment with pip, conda, poetry, or docker! You can set up the keys for the different providers in a `config.py` as recommended in the book. Please check the [setup instructions](../SETUP.md) for dependencies and API keys before you start.

## Notebooks

| Notebook | Description | Colab | Kaggle | Gradient |
|----------|-------------|-------|--------|----------|
| [01_embeddings_and_vectorstores.ipynb](01_embeddings_and_vectorstores.ipynb) | Explores embeddings creation and vector storage fundamentals for RAG systems | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]() | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)]() | [![Gradient](https://assets.paperspace.io/img/gradient-badge.svg)]() |
| [02_document_processing.ipynb](02_document_processing.ipynb) | Demonstrates document loading and chunking strategies for optimal retrieval | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]() | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)]() | [![Gradient](https://assets.paperspace.io/img/gradient-badge.svg)]() |
| [03_retrieval_techniques.ipynb](03_retrieval_techniques.ipynb) | Covers different retrieval methods including vector search, hybrid search, and MMR | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]() | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)]() | [![Gradient](https://assets.paperspace.io/img/gradient-badge.svg)]() |
| [04_advanced_rag_techniques.ipynb](04_advanced_rag_techniques.ipynb) | Advanced techniques like query transformation, contextual compression, and self-consistency checking | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]() | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)]() | [![Gradient](https://assets.paperspace.io/img/gradient-badge.svg)]() |

## Streamlit Application

| Application | Description | Colab | Kaggle | Gradient |
|-------------|-------------|-------|--------|----------|
| [streamlit_app.py](streamlit_app.py) | Complete RAG application with citations for corporate documentation | x | x | x |

The Streamlit application demonstrates a complete RAG pipeline for corporate documentation, including document loading, retrieval, generation, and verification.

## Running the Streamlit App

The imports require the `PYTHONPATH` environment variable to include the repository root. 

If you run from the repository root, run like this:
```bash
PYTHONPATH=. streamlit run chapter4/streamlit_app.py
```

If you run this from the `chapter4` directory, run as follows - with a change to `PYTHONPATH`:
```bash
PYTHONPATH=../ streamlit run streamlit_app.py
```

## Data Files

The repository includes sample data for running the examples:

| File | Description |
|------|-------------|
| [knowledge_base.json](data/knowledge_base.json) | Sample knowledge base with information about AI models and techniques |


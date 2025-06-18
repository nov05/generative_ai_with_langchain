# Chapter 3 - Building Workflows with LangGraph

Please make sure, you set up your environment with pip, conda, poetry, or docker!

You can set up the keys for the different providers with a `config.py` like this:
```python
import os

def set_environment():
    os.environ["OPENAI_API_KEY"] = "... "  # <- this has to be your api key!
    # I'm omitting all other keys
```

You can subsequently set all these keys for LangChain importing and executing the `set_environment()` function in your projects or notebooks:
```python
from config import set_environment
set_environment()
```

| Section	| File | Colab	 | Kaggle	| Gradient |
|-----------|--------|--------|-----------|----------|
| Intro to LangGraph |  [notebook](langgraph_intro.ipynb)   | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/benman1/generative_ai_with_langchain/blob/second_edition/langgraph_intro.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/notebooks/create?source=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/langgraph_intro.ipynb) | [![Gradient](https://img.shields.io/badge/Gradient-Open-blue)](https://gradient.run/notebooks/new?template=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/langgraph_intro.ipynb) |
| Output parsers |  [notebook](output_parsers.ipynb.ipynb)   | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/benman1/generative_ai_with_langchain/blob/second_edition/output_parsers.ipynb.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/notebooks/create?source=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/output_parsers.ipynb.ipynb) | [![Gradient](https://img.shields.io/badge/Gradient-Open-blue)](https://gradient.run/notebooks/new?template=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/output_parsers.ipynb.ipynb) |
| Error handling | [notebook](error_handling.ipynb)  | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/benman1/generative_ai_with_langchain/blob/second_edition/error_handling.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/notebooks/create?source=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/error_handling.ipynb) | [![Gradient](https://img.shields.io/badge/Gradient-Open-blue)](https://gradient.run/notebooks/new?template=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/error_handling.ipynb) |
| Prompt templates | [notebook](prompt-templates.ipynb)     | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/benman1/generative_ai_with_langchain/blob/second_edition/prompt-templates.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/notebooks/create?source=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/prompt-templates.ipynb) | [![Gradient](https://img.shields.io/badge/Gradient-Open-blue)](https://gradient.run/notebooks/new?template=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/prompt-templates.ipynb) |
| Multimodaliry | [notebook](multimodality.ipynb)   | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/benman1/generative_ai_with_langchain/blob/second_edition/multimodality.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/notebooks/create?source=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/multimodality.ipynb) | [![Gradient](https://img.shields.io/badge/Gradient-Open-blue)](https://gradient.run/notebooks/new?template=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/multimodality.ipynb) |
| Map-reduce approach to handle long inputs |  [notebook](map_reduce.ipynb)  | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/benman1/generative_ai_with_langchain/blob/second_edition/map_reduce.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/notebooks/create?source=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/map_reduce.ipynb) | [![Gradient](https://img.shields.io/badge/Gradient-Open-blue)](https://gradient.run/notebooks/new?template=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/map_reduce.ipynb) |
| Memory |  [notebook](memory.ipynb)  | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/benman1/generative_ai_with_langchain/blob/second_edition/memory.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/notebooks/create?source=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/memory.ipynb) | [![Gradient](https://img.shields.io/badge/Gradient-Open-blue)](https://gradient.run/notebooks/new?template=https://github.com/benman1/generative_ai_with_langchain/blob/second_edition/memory.ipynb) |  
| Self-consistency | [notebook](self_consistency.ipynb) | - | - | - |
  
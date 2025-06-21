
* [General notes](https://docs.google.com/document/d/1weC8RowQGk59pVyfBUwmcf3lb6yDYPqw2Hc6QxkNKuM)   
* [**Colab notebooks**](https://drive.google.com/drive/u/1/folders/1ymnY4ek6FJIviQRkI7CZnAgoMlxLwuGN) (Chapter 2-8, notebooks in Colab) ✅  
  * Note:   
    Numerous small updates — including API adjustments, bug fixes, added comments and notes, and formatting improvements—have been made to the original Jupyter notebooks to enhance clarity and ensure reproducibility, especially when running them in `Google Colab`.  
* [**Applications**](https://github.com/nov05/generative_ai_with_langchain/tree/second_edition/chapter9) (Chapter 9, run locally) ✅   
  * Note:  
    The `requirements.txt` has been updated, [the `.devcontainer` folder](https://github.com/nov05/generative_ai_with_langchain/tree/second_edition/.devcontainer) added to the repository, and minor bug fixes and changes applied to the original code.  
* Environments:
  * For Jupyter notebooks: `Google Colab` (free version)
  * For local applications: `Windows 11`, `VS Code` with `Dev Container`, `Docker Desktop`, `WSL2` (Ubuntu-22.04)  
  * Model related services: `LangSmith` APIs, `Google Cloud Platform` (GCP, with billing account, service account, VertexAI APIs), `OpenAI` APIs (with billing), `Anthropic` APIs (with billing), `Mistral AI` APIs, `Replicate` APIs (with [billing](https://replicate.com/account/billing)), `Stability AI` APIs (with [billing](https://platform.stability.ai/account/credits)), `HuggingFace` APIs   
  
    [<img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/icons/youtube_red_2000x2000.png" width=20> Create Dev Container](https://youtu.be/HtXdJ5J0DLY?t=25)  

<br>  

### 👉 **Highlights**


* **Chapter 9** (locally, off notebook, in VS Code Dev Container) 

  * Web application 1, **Build a chatbot** with `FastAPI`, `WebSocket`, and `Claude APIs` (model="claude-3-opus-20240229")  
    [<img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/icons/youtube_red_2000x2000.png" width=20> Watch the demo video](https://youtu.be/HtXdJ5J0DLY)  

    * Prerequisites: You have `Docker Desktop` and `WSL2` installed, and Docker set to use Linux containers.  
    * Create `config.py` in the `<repo>/chapter9/fastapi` directory (refer to `config_example.py`).  
    * In `VS Code`: Press `F1` -> Choose `Dev Containers: Rebuild Container` (It takes about 15 minutes to build.)
    * Menu: `Terminal` -> `New Terminal` (Make sure it is `bash - generative_ai_with_langchain`.) 
      ```python
      ## Launch the app
      $ cd chapter9/fastapi
      $ python main.py
      ```
    * Open http://localhost:8000/ in the browser.

      <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-18%2015_52_12-Chatbot%20Playground_chapter9.jpg" width=800>

  <br>  

  * Web application 2, **Build a search tool** with `HuggingFace` embedding ("sentence-transformers/all-MiniLM-L6-v2"), `FAISS` (vectore store for RAG), `Ray` (Distributed computing, Serve), `FastAPI`

    * Enable CUDA, and install torch versions for GPU in the Dockerfile.
    * In a Dev Container terminal, build index and the index will be saved under `/faiss_index`
      ```python
      $ cd chapter9/ray
      $ python build_index.py
      ```
      <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-20%2018_44_11-chapter9_ray_build_faiss_index.jpg" width=800>  

    <br>  

    * Run `$ python serve_index.py` to deploy the app, or do it in bash.
      ```python
      $ ray stop --force
      $ ray start --head
      $ serve deploy serve_index.yaml
      ```

    * Run queries via url, or run `$ python test_client.py` to test the app.  
      E.g.  
      http://localhost:8000/?query=How%20can%20Ray%20help%20with%20deploying%20LLMs%3F  
      http://localhost:8000/search?query=How%20can%20Ray%20help%20with%20deploying%20LLMs%3F&n_results=3   

      <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-21%2000_46_40-localhost_8000_search_query%3DHow%20can%20Ray%20help%20with%20deploying%20LLMs%253F%26n_results%3D3.jpg" width=800>  

    <br>  

    * Check the Ray Serve dashboard at http://localhost:8265

      <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-21%2000_50_06-ray%20serve%20dashboard.jpg" width=800>  
 
  <br>  

  * Observability tools 
  
    * [Prompt tracking with `promptwatch`](https://github.com/nov05/generative_ai_with_langchain/blob/second_edition/chapter9/tools/prompt_tracking.py)   
    * [Trace and assess with `LangChain` ReAct agent](https://github.com/nov05/generative_ai_with_langchain/blob/second_edition/chapter9/tools/tracing.py)  

<br>

* **Chapter 2** 

  * [Notebook 5, multi-model](https://github.com/nov05/Google-Colaboratory/blob/master/generative_ai_with_langchain/20250602_05_multimodal_(Image_generation_and_understanding).ipynb)  

  E.g. Generate image from text prompt  

  <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-04%2005_02_33-Settings.jpg" width=800>  

    E.g. Describe a video in text    

  <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-04%2005_03_15-Settings.jpg" width=800>  

<br>  

* **Chapter 3**

  * [Notebook 6, map-reduce](https://drive.google.com/file/d/18lTgJJzWF9THjxbO5Qm8-T00Wf7AQCAx)  

    * E.g. Process a 4-minute video and generate a summary ([Check the result](https://nbviewer.org/github/nov05/generative_ai_with_langchain/blob/second_edition/chapter3/20250605_map_reduce_02.ipynb))  

    * E.g. Process a 10-minute video and generate a summary       

  <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-05%2001_07_35-20250604_map_reduce.ipynb%20-%20Colab.jpg" width=800>   

  <br>  

  * [Notebook 8](https://drive.google.com/file/d/1kDf2t02MfRPa89kMOtw73-uxqWDqBd8F), using `LangSmith` tracing to log model performance 

  <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-13%2006_11_56-generative_ai_with_langchain%20-%20LangSmith.jpg" width=800> 


<br>  

* [**Chapter 4**](https://drive.google.com/drive/folders/1Bgeuq4lJLkV-_rMOBgUNTGL3GVrHh71h)      

  * OpenAI embeddings
  * `Chroma` and `FAISS` vector stores
  * Similarity search, max marginal relevance search, KNN retriever, PubMed retriever (external search API retriever), Query expansion, Hypothetical Document Embeddings (HyDE), Contextual Compression, Source Attribution, Self-consistency Checking    

<br>  

* **Chapter 5**

  * [Notebook 5, ReAct examples](https://drive.google.com/file/d/1fljLPYufX-8DUDwXVUdtiS3JTIxcbmgE)     

  <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-10%2012_35_24-05_react_example.ipynb%20-%20Colab.jpg" width=800>
 
  <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-11%2001_23_40-05_react_example.ipynb%20-%20Colab.jpg" width=800>   

<br>  

* **Chapter 6**

  * [Notebook 1, Multi-agent system](https://drive.google.com/file/d/1vAYX1buFY0nq79MgbvdJxp3-WPBfmi2p), e.g. research and critique agents    

  <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-11%2013_51_33-01_Multiple-choice%20question-answering%20agent.ipynb%20-%20Colab.jpg" width = 800>    

  <br>  

  * Notebook 4, **Tree-of-Thoughts (ToT)** example (naive, without Monte Carlo tree search) ([GitHub copy with nbviwer](https://nbviewer.org/github/nov05/Google-Colaboratory/blob/master/generative_ai_with_langchain/04_Tree_of_thoughts_%28ToT%29_agent.ipynb), [my post](https://www.linkedin.com/posts/wenjingliu7_langchain-treeofthoughts-llm-activity-7340456103966646273-zkJ6/))         

  <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-12%2013_07_49-04_Tree-of-thoughts%20(ToT)%20agent.ipynb%20-%20Colab.jpg" width=800>


<br>  

* **Chapter 7**

  * [Notebook 4, Build a RAG on a documentation website](https://github.com/nov05/Google-Colaboratory/blob/master/generative_ai_with_langchain/04_langchain_rag.ipynb)  

  <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-13%2017_15_16-04_langchain_rag.ipynb%20-%20Colab.jpg" width=800>   

  <br>  

  * [Notebook 5, Data Science (agent for Pandas dataframe)](https://github.com/nov05/Google-Colaboratory/blob/master/generative_ai_with_langchain/07_05_data_science.ipynb)  

  <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-13%2018_40_45-07_05_data_science.ipynb%20-%20Colab.jpg" width=800>   

<br>

* **Chapter 8**

  * [Notebook 2, advanced evaluation](https://nbviewer.org/github/nov05/Google-Colaboratory/blob/master/generative_ai_with_langchain/08_02_advanced_evaluation.ipynb)   

  <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-13%2022_42_52-chapter%208%20notebook%202%20langsmith%20eval%20trajectory.jpg" width=800>

  * [Notebook 3, `LangSmith` evaluation](https://nbviewer.org/github/nov05/Google-Colaboratory/blob/master/generative_ai_with_langchain/08_03_langsmith_evaluation.ipynb)  

  Insurance claim text exaction example   
  <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-14%2002_59_42-08_03_insurance%20claim%20text%20extraction.jpg" width=800>   

  Tracing with `LangSmith`   
  <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-14%2002_56_11-08_03_langsmith_eval_insurance_claim_text_extraction_.jpg" width=800>

<br>    

### 👉 **Create enviroment variables for API keys**    

  * Locally, create `config.py` and place it at the right directories.   

    ```python
    import os
    def set_environment():
        os.environ["ANTHROPIC_API_KEY"] = (
            "..."
        )
        ## And/Or other API Keys
        ...
    ```
  <br>  

  * In `Google Colab`, store the API keys as secrets.  

    <img src="https://raw.githubusercontent.com/nov05/pictures/refs/heads/master/generative_ai_with_langchain/2025-06-18%2016_18_34-Settings.jpg" width=800>   


<br>  

### 👉 **Logs**  

2025-06-02 Repo forked
2025-06-16 All notebooks (Chapter 1-8) done

<br><br><br>  

---  

<h1 align="center">
Generative AI with LangChain, Second Edition</h1>
<p align="center">This is the code repository for <a href ="https://www.packtpub.com/en-us/product/generative-ai-with-langchain-second-edition-9781837022014"> Generative AI with LangChain, Second Edition</a>, published by Packt.
</p>

<h2 align="center">
Build production ready LLM applications and advanced agents using Python and LangGraph 
</h2>
<p align="center">
Ben Auffarth, Leonid Kuligin</p>

<p align="center">
   <a href="https://discord.gg/YQbX5rsc74" alt="Discord" title="Learn more on the Discord server"><img width="32px" src="https://cliply.co/wp-content/uploads/2021/08/372108630_DISCORD_LOGO_400.gif"/></a>
  &#8287;&#8287;&#8287;&#8287;&#8287;
  <a href="https://packt.link/free-ebook/9781837022014"><img width="32px" alt="Free PDF" title="Free PDF" src="https://cdn-icons-png.flaticon.com/512/4726/4726010.png"/></a>
 &#8287;&#8287;&#8287;&#8287;&#8287;
  <a href="https://packt.link/gbp/9781837022014"><img width="32px" alt="Graphic Bundle" title="Graphic Bundle" src="https://cdn-icons-png.flaticon.com/512/2659/2659360.png"/></a>
  &#8287;&#8287;&#8287;&#8287;&#8287;
   <a href="https://amzn.to/4dErkya"><img width="32px" alt="Amazon" title="Get your copy" src="https://cdn-icons-png.flaticon.com/512/15466/15466027.png"/></a>
  &#8287;&#8287;&#8287;&#8287;&#8287;
</p>
<details open> 
  <summary><h2>About the book</summary>
<a href="https://www.packtpub.com/en-us/product/generative-ai-with-langchain-9781837022014">
<img src="https://content.packt.com/B32363/cover_image_small.jpg" alt="Generative AI with LangChain, 2nd Edition (2025)" height="256px" align="right">
</a>

This second edition tackles the biggest challenge facing companies in AI today: moving from prototypes to production. Fully updated to reflect the latest developments in the LangChain ecosystem, it captures how modern AI systems are developed, deployed, and scaled in enterprise environments. This edition places a strong focus on multi-agent architectures, robust LangGraph workflows, and advanced retrieval-augmented generation (RAG) pipelines.
You'll explore design patterns for building agentic systems, with practical implementations of multi-agent setups for complex tasks. The book guides you through reasoning techniques such as Tree-of -Thoughts, structured generation, and agent handoffs—complete with error handling examples. Expanded chapters on testing, evaluation, and deployment address the demands of modern LLM applications, showing you how to design secure, compliant AI systems with built-in safeguards and responsible development principles. This edition also expands RAG coverage with guidance on hybrid search, re-ranking, and fact-checking pipelines to enhance output accuracy.
Whether you're extending existing workflows or architecting multi-agent systems from scratch, this book provides the technical depth and practical instruction needed to design LLM applications ready for success in production environments.
</details>
<details open> 
  <summary><h2>Key Learnings</summary>

<ul>
<li>Design and implement refined multi-agent systems using LangGraph</li>
<li>Enterprise-grade testing and evaluation frameworks for LLM applications</li>
<li>Deploy production-ready observability and monitoring solutions</li>
<li>Build RAG systems with hybrid search and re-ranking capabilities</li>
<li>Implement agents for software development and data analysis</li>
<li>Work with latest LLMs and providers Google Gemini, Anthropic and Mistral, DeepSeek, and OpenAI o3-mini</li>
<li>Optimize cost and performance across different deployment types</li>
<li>Design secure, compliant AI systems with current best practices</li>
</ul>

  </details>
  <details open>
<summary><h2>Note to Readers</summary>

Thank you for choosing "Generative AI with LangChain"! We appreciate your enthusiasm and feedback.

Please note that we've released several updated versions of the book. Consequently, there are three different branches for this repository: 
* [2nd edition](https://github.com/benman1/generative_ai_with_langchain/tree/second_edition) - this is for the 2nd edition of the book, corresponding to ver 0.3 of LangChain.
* [softupdate](https://github.com/benman1/generative_ai_with_langchain/tree/softupdate) - this is for the soft update of the book (2024), corresponding to ver 0.1.13 of LangChain.
* [main](https://github.com/benman1/generative_ai_with_langchain/tree/main) - this is the original version of the book (December 2023).

Please refer to the version that you are interested in or that corresponds to your version of the book.
</details>

<details open>
<summary><h3>Download a free PDF <img alt="Coding" height="25" width="40" src="https://emergency.com.au/wp-content/uploads/2021/03/free.gif"></summary>
Download a free PDF <img alt="Coding" height="25" width="40" src="https://emergency.com.au/wp-content/uploads/2021/03/free.gif">

_If you have already purchased an up-to-date print or Kindle version of this book, you can get a DRM-free PDF version at no cost. Simply click on the link to claim your free PDF._
[Free-Ebook](https://packt.link/free-ebook/9781837022014) <img alt="Coding" height="15" width="35"  src="https://media.tenor.com/ex_HDD_k5P8AAAAi/habbo-habbohotel.gif">

We  provide a PDF file that has color images of the screenshots/diagrams used in this book at [GraphicBundle](https://packt.link/gbp/9781837022014) <img alt="Coding" height="15" width="35"  src="https://media.tenor.com/ex_HDD_k5P8AAAAi/habbo-habbohotel.gif">
</details>

<details open>
<summary><h3>Commitment</summary>

<b>Code Updates:</b> Our commitment is to provide you with stable and valuable code examples. While LangChain is known for frequent updates, we understand the importance of aligning our code with the latest changes. The companion repository is regularly updated to harmonize with LangChain developments.

<b>Expect Stability:</b> For stability and usability, the repository might not match every minor LangChain update. We aim for consistency and reliability to ensure a seamless experience for our readers. 

<b>How to Reach Us:</b> Encountering issues or have suggestions? Please don't hesitate to open an issue, and we'll promptly address it. Your feedback is invaluable, and we're here to support you in your journey with LangChain.
Thank you for your understanding and happy coding!
</details>

<details open> 
   <summary><h3>Know more on the Discord server <img alt="Coding" height="25" width="32"  src="https://cliply.co/wp-content/uploads/2021/08/372108630_DISCORD_LOGO_400.gif"></summary>

You can engage with the author and other readers on the discord server and find latest updates and discussions in the community at [Discord](https://discord.gg/YQbX5rsc74)
</details>

<details open> 
  <summary><h2>Chapters</summary>

In the following table, you can find links to the directories in this repository. Each directory contains further links to python scripts and to notebooks. You can also see links to computing platforms, where you can execute the notebooks in the repository. Please note that there are other Python scripts and projects that are not notebooks, which you'll find in the chapter directories.

| Chapter | Title | Directory Link |
|---------|-------|----------------|
| Chapter 1 | The Rise of Generative AI: From Language Models to Agents | [chapter1/](./chapter1) |
| Chapter 2 | First Steps with LangChain | [chapter2/](./chapter2) |
| Chapter 3 | Building Workflows with LangGraph | [chapter3/](./chapter3) |
| Chapter 4 | Building Intelligent RAG Systems with LangChain | [chapter4/](./chapter4) |
| Chapter 5 | Building Intelligent Agents | [chapter5/](./chapter5) |
| Chapter 6 | Advanced Applications and Multi-Agent Systems | [chapter6/](./chapter6) |
| Chapter 7 | Software Development and Data Analysis Agents | [chapter7/](./chapter7) |
| Chapter 8 | Evaluation and Testing of LLM Applications | [chapter8/](./chapter8) |
| Chapter 9 | Production Deployment and Observability | [chapter9/](./chapter9) |

</details>


<details open> 
  <summary><h2>Requirements for this book</summary>
  
### Software and hardware list
This is the companion repository for the book. Here are a few instructions that help getting set up. Please also see chapter 2. 

All chapters rely on Python. 

Please check the instructions for setting up the environment either in the book or [here](./SETUP.md). They include instructions for dependencies and API keys. **Following the instructions should make sure that you don't have any issues running the code in the book or this repository. If you encounter any issues, please make sure you've followed these instructions.**


## 👋 Contribute

We welcome contributions from developers of all levels. If you'd like to contribute, please check our [contributing guidelines](./CONTRIBUTING.md) and help make this repository and the book more accessible.

---
[![Star History Chart](https://api.star-history.com/svg?repos=benman1/generative_ai_with_langchain&type=Timeline)](https://star-history.com/#benman1/generative_ai_with_langchain&Date)


## ❤️ Contributors

[![repo contributors](https://contrib.rocks/image?repo=benman1/generative_ai_with_langchain)](https://github.com/benman1/generative_ai_with_langchain/graphs/contributors)


<details> 
  <summary><h2>Get to know Authors</h2></summary>

_Ben Auffarth_ Ben Auffarth is a full-stack data scientist with more than 15 years of work experience. With a background and Ph.D. in computational and cognitive neuroscience, he has designed and conducted wet lab experiments on cell cultures, analyzed experiments with terabytes of data, run brain models on IBM supercomputers with up to 64k cores, built production systems processing hundreds and thousands of transactions per day, and trained language models on a large corpus of text documents. He co-founded and is the former president of Data Science Speakers, London.

_Leonid Kuligin_ Leonid Kuligin is a staff AI engineer at Google Cloud, working on generative AI and classical machine learning solutions (such as demand forecasting or optimization problems). Leonid is one of the key maintainers of Google Cloud integrations on LangChain, and a visiting lecturer at CDTM (TUM and LMU). Prior to Google, Leonid gained more than 20 years of experience in building B2C and B2B applications based on complex machine learning and data processing solutions such as search, maps, and investment management in German, Russian, and US technological, financial, and retail companies.



</details>

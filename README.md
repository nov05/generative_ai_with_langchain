* [General notes](https://docs.google.com/document/d/1weC8RowQGk59pVyfBUwmcf3lb6yDYPqw2Hc6QxkNKuM)   
* [**Colab notebooks**](https://drive.google.com/drive/u/1/folders/1ymnY4ek6FJIviQRkI7CZnAgoMlxLwuGN) ✅  
  *Note: Numerous minor changes, bug fixes, comments, and notes have been added to the original Jupyter notebooks to improve clarity and ensure reproducibility, especially when running them in `Google Colab`.*  

<br>  

### **Detailed Feature Summary**

This book provides comprehensive coverage of building production-ready LLM applications and advanced agents using Python, LangChain, and LangGraph. Key features and topics include:

*   **Chapter 1: The Rise of Generative AI:** Introduces foundational concepts of Generative AI, Large Language Models (LLMs), and the LangChain framework.
*   **Chapter 2: First Steps with LangChain:** Covers practical setup, basic LangChain components (Models, Prompts, Parsers), and building simple LLM chains. Includes examples like text generation (e.g., from text prompts to generate images) and describing videos in text.
*   **Chapter 3: Building Workflows with LangGraph:** Focuses on creating complex workflows and agentic systems using LangGraph. Demonstrates map-reduce techniques for tasks like video summarization (e.g., processing 4-minute and 10-minute videos).
*   **Chapter 4: Building Intelligent RAG Systems with LangChain:** Explores Retrieval Augmented Generation (RAG) techniques, including OpenAI embeddings, vector stores (`Chroma`, `FAISS`), various search strategies (similarity, max marginal relevance, KNN), external search API integration (PubMed retriever), query expansion, Hypothetical Document Embeddings (HyDE), contextual compression, source attribution, and self-consistency checking.
*   **Chapter 5: Building Intelligent Agents:** Delves into the design and implementation of intelligent agents, their reasoning capabilities (e.g., Tree-of-Thoughts), structured generation, and decision-making processes, including agent handoffs and error handling.
*   **Chapter 6: Advanced Applications and Multi-Agent Systems:** Discusses advanced LangChain applications and the development of multi-agent systems for complex problem-solving, emphasizing design patterns for agentic systems.
*   **Chapter 7: Software Development and Data Analysis Agents:** Presents agents specifically designed for software development tasks and data analysis.
*   **Chapter 8: Evaluation and Testing of LLM Applications:** Covers enterprise-grade frameworks and methodologies for testing and evaluating the performance, reliability, and security of LLM applications.
*   **Chapter 9: Production Deployment and Observability:** Guides on deploying LLM applications into production environments, including monitoring, observability, cost/performance optimization, and ensuring secure, compliant AI systems with built-in safeguards and responsible development principles. Also covers working with various LLM providers like Google Gemini, Anthropic, Mistral, DeepSeek, and OpenAI o3-mini.

<br>

### **Important Notes for Users**

*   **Repository Branches:** This repository has multiple branches corresponding to different editions and updates of the book:
    *   [`second_edition`](https://github.com/benman1/generative_ai_with_langchain/tree/second_edition): For the 2nd edition of the book (LangChain v0.3). This is the active branch for current development.
    *   [`softupdate`](https://github.com/benman1/generative_ai_with_langchain/tree/softupdate): For the soft update (2024, LangChain v0.1.13).
    *   [`main`](https://github.com/benman1/generative_ai_with_langchain/tree/main): For the original version of the book (December 2023).
    Please ensure you are using the branch that aligns with your book version and LangChain setup.
*   **Colab Notebooks:** Many examples are provided as Jupyter notebooks. Numerous minor changes, bug fixes, comments, and notes have been added to these notebooks to improve clarity and ensure reproducibility, especially when running them in `Google Colab`. You can find direct links to these Colab notebooks [here](https://drive.google.com/drive/u/1/folders/1ymnY4ek6FJIviQRkI7CZnAgoMlxLwuGN).
*   **Setup and Dependencies:** For a smooth experience, please refer to the detailed setup instructions in Chapter 2 of the book or the `SETUP.md` file in this repository. Following these instructions carefully will help avoid common issues with dependencies and API keys.
*   **Code Stability and Updates:** LangChain is a rapidly evolving library. While we strive to keep the repository updated with significant LangChain developments, our primary goal is to provide stable, reliable, and valuable code examples that align with the book's content. Therefore, the repository might not always match every minor LangChain update. We aim for consistency to ensure a seamless learning experience.
*   **Getting Support:** If you encounter issues, have suggestions, or questions, please do not hesitate to open an issue on GitHub. Your feedback is invaluable. You can also engage with the authors and other readers on the [Discord server](https://discord.gg/YQbX5rsc74) for discussions and latest updates.
*   **Free Resources:** If you have purchased an up-to-date print or Kindle version of this book, you can get a DRM-free PDF version at no cost via [Packt's website](https://packt.link/free-ebook/9781837022014). Additionally, a graphic bundle containing color images of the screenshots and diagrams used in this book is available at [Packt's Graphic Bundle page](https://packt.link/gbp/9781837022014).

<br>  

### **Logs**  

2025-06-02 repo forked

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
<summary><h2>Note to Readers - Combined into "Important Notes for Users"</h2>

<!--
Thank you for choosing "Generative AI with LangChain"! We appreciate your enthusiasm and feedback.

Please note that we've released several updated versions of the book. Consequently, there are three different branches for this repository: 
* [2nd edition](https://github.com/benman1/generative_ai_with_langchain/tree/second_edition) - this is for the 2nd edition of the book, corresponding to ver 0.3 of LangChain.
* [softupdate](https://github.com/benman1/generative_ai_with_langchain/tree/softupdate) - this is for the soft update of the book (2024), corresponding to ver 0.1.13 of LangChain.
* [main](https://github.com/benman1/generative_ai_with_langchain/tree/main) - this is the original version of the book (December 2023).

Please refer to the version that you are interested in or that corresponds to your version of the book.
-->
</details>

<details open>
<summary><h3>Download a free PDF <img alt="Coding" height="25" width="40" src="https://emergency.com.au/wp-content/uploads/2021/03/free.gif"></summary>
Download a free PDF <img alt="Coding" height="25" width="40" src="https://emergency.com.au/wp-content/uploads/2021/03/free.gif">

_If you have already purchased an up-to-date print or Kindle version of this book, you can get a DRM-free PDF version at no cost. Simply click on the link to claim your free PDF._
[Free-Ebook](https://packt.link/free-ebook/9781837022014) <img alt="Coding" height="15" width="35"  src="https://media.tenor.com/ex_HDD_k5P8AAAAi/habbo-habbohotel.gif">

We  provide a PDF file that has color images of the screenshots/diagrams used in this book at [GraphicBundle](https://packt.link/gbp/9781837022014) <img alt="Coding" height="15" width="35"  src="https://media.tenor.com/ex_HDD_k5P8AAAAi/habbo-habbohotel.gif">
</details>

<details open>
<summary><h3>Commitment - Combined into "Important Notes for Users"</h3>
<!--
<b>Code Updates:</b> Our commitment is to provide you with stable and valuable code examples. While LangChain is known for frequent updates, we understand the importance of aligning our code with the latest changes. The companion repository is regularly updated to harmonize with LangChain developments.

<b>Expect Stability:</b> For stability and usability, the repository might not match every minor LangChain update. We aim for consistency and reliability to ensure a seamless experience for our readers. 

<b>How to Reach Us:</b> Encountering issues or have suggestions? Please don't hesitate to open an issue, and we'll promptly address it. Your feedback is invaluable, and we're here to support you in your journey with LangChain.
Thank you for your understanding and happy coding!
-->
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

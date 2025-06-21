"""Prompt tracking with PromptWatch.io."""
from langchain.callbacks.base import BaseCallbackHandler
import promptwatch
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
# https://pypi.org/project/promptwatch/
from promptwatch import PromptWatch
# Local imports
from config import set_environment


# Set up environment variables
set_environment()
print(f"promptwatch version: {promptwatch.__version__}")  # 0.4.5


# Setup the chain using the modern Runnables API
prompt_template = PromptTemplate.from_template("Finish this sentence :{input}")
llm = ChatOpenAI()
chain = prompt_template | llm | StrOutputParser()

# Track prompt execution with PromptWatch
# https://docs.promptwatch.io/docs/quickstart/
with PromptWatch() as pw:
    result = chain.invoke(
        {"input": "The quick brown fox jumped over"},
    )
    print(f"👉 Result: {result}")

print("Check PromptWatch.io dashboard for detailed trace information")


# Nov05: Example output (Ignore the error messages from LangChain caused by PromptWatch)
'''
root ➜ /workspaces/generative_ai_with_langchain/chapter9/tools (second_edition) $ python prompt_tracking.py
promptwatch version: 0.4.5
Error in LangChainCallbackHandler.on_chain_start callback: AttributeError("'NoneType' object has no attribute 'get'")
Error in LangChainCallbackHandler.on_chain_start callback: AttributeError("'NoneType' object has no attribute 'get'")
Error in LangChainCallbackHandler.on_chain_end callback: AttributeError("'NoneType' object has no attribute 'outputs'")
Error in LangChainCallbackHandler.on_chain_end callback: AttributeError("'NoneType' object has no attribute 'outputs'")
👉 Result:  the lazy dog.
Check PromptWatch.io dashboard for detailed trace information
'''

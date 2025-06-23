"""Agent functionality."""
# Code updated by Nov05 on 2025-06-23

import pandas as pd
from langchain.agents import AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_openai import ChatOpenAI
# Local imports
from prompts import PROMPT
from config import set_environment
set_environment()


def create_agent(csv_file: str) -> AgentExecutor:
    """
    Create data agent.

    Args:
        csv_file: The path to the CSV file.

    Returns:
        An agent executor.
    """
    llm = ChatOpenAI()
    df = pd.read_csv(csv_file)
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        # allow_dangerous_code=True,  # Warning: No longer supported
        handle_parsing_errors=True,
    )
    return agent


def query_agent(agent: AgentExecutor, query: str) -> str:
    """Query an agent and return the response."""
    prompt = PromptTemplate(template=PROMPT, input_variables=["query"])
    formatted_prompt = prompt.format(query=query)
    return agent.run(formatted_prompt)

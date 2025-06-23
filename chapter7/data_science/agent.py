"""Agent functionality."""
# Code updated by Nov05 on 2025-06-23

from langchain.chat_models import ChatOpenAI
import pandas as pd
from langchain.agents import AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
# from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
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
        allow_dangerous_code=True,
        # handle_parsing_errors = True,  # Warning: No longer supported
        agent_executor_kwargs={
            "handle_parsing_errors": True,  # Warning: No longer supported
        },
    )
    return agent


class DataAgent:
    def __init__(self,
                 csv_file: str,
                 llm=ChatOpenAI(),
                 verbose: bool = True,
                 allow_dangerous_code: bool = True):
        """
        Initialize the data agent with a CSV file.

        Args:
            csv_file: Path to the CSV file.
            verbose: Whether to enable verbose output.
            allow_dangerous_code: Whether to allow execution of arbitrary Python code.
        """
        self.csv_file = csv_file
        self.llm = llm
        self.verbose = verbose
        self.allow_dangerous_code = allow_dangerous_code
        self.df = pd.read_csv(self.csv_file)
        self.agent = create_pandas_dataframe_agent(
            self.llm,
            self.df,
            verbose=self.verbose,
            allow_dangerous_code=self.allow_dangerous_code,
            agent_executor_kwargs={
                "handle_parsing_errors": True
            },
        )

    def __getattr__(self, name):
        """Delegate all other attributes/methods to self.agent."""
        return getattr(self.agent, name)


def query_agent(agent: AgentExecutor, query: str) -> str:
    """Query an agent and return the response."""
    prompt = PromptTemplate(template=PROMPT, input_variables=["query"])
    formatted_prompt = prompt.format(query=query)
    # return agent.run(formatted_prompt)
    return agent.invoke(formatted_prompt)


# Added by Nov05
def query_agent_with_stream(agent: AgentExecutor, query: str):
    prompt = PromptTemplate(template=PROMPT, input_variables=["query"])
    formatted_prompt = prompt.format(query=query)
    for event in agent.stream(formatted_prompt):
        # Each `event` is a dict, e.g., {"steps":[...], "messages": [...]}
        print(event)
        yield event

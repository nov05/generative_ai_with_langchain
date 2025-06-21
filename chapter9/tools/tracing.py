"""Tracing of agent calls and intermediate results."""
# Code updated by Nov05 on 2025-06-21

import subprocess
from urllib.parse import urlparse
# from langchain.agents import AgentType, initialize_agent
# from langchain_core.tools import StructuredTool
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langchain_openai.chat_models import ChatOpenAI
from pydantic import HttpUrl
# Local imports
from config import set_environment
set_environment()


@tool
def ping(url: HttpUrl, return_error: bool) -> str:
    """Ping the fully specified url. Must include https:// in the url."""
    hostname = urlparse(str(url)).netloc
    completed_process = subprocess.run(
        ["ping", "-c", "1", hostname], capture_output=True, text=True
    )
    output = completed_process.stdout
    if return_error and completed_process.returncode != 0:
        return completed_process.stderr
    return output


# alternatively annotate the ping() function with @tool
# ping_tool = StructuredTool.from_function(ping)
llm = ChatOpenAI(
    # model="gpt-3.5-turbo-0613",  # Nov05: deprecated
    temperature=0
)
# agent = initialize_agent(
#     llm=llm,
#     tools=[ping_tool],
#     agent=AgentType.OPENAI_MULTI_FUNCTIONS,
#     return_intermediate_steps=True,  # IMPORTANT!
# )
agent = create_react_agent(llm, tools=[ping])
# result = agent("What's the latency like for https://langchain.com?")
# print(result)
query = "What's the latency like for `https://langchain.com`?"
print("\n👉 Stream agent responses:")
for event in agent.stream({"messages": [("user", query)]}, stream_mode="values"):
    event["messages"][-1].pretty_print()
result = agent.invoke({"messages": [("user", query)]})
print("\n👉 Result:")
print(result)


if __name__ == "__main__":

    pass


# Nov05: Example output
'''
root ➜ /workspaces/generative_ai_with_langchain/chapter9/tools (second_edition) $ python tracing.py

👉 Stream agent responses:
================================ Human Message =================================

What's the latency like for `https://langchain.com`?
================================== Ai Message ==================================
Tool Calls:
  ping (call_JNa2YS7sJY9aU0Jt5JQPezZE)
 Call ID: call_JNa2YS7sJY9aU0Jt5JQPezZE
  Args:
    url: https://langchain.com
    return_error: True
================================= Tool Message =================================
Name: ping

PING langchain.com (99.83.190.102) 56(84) bytes of data.
64 bytes from 99.83.190.102 (99.83.190.102): icmp_seq=1 ttl=63 time=63.2 ms

--- langchain.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 63.221/63.221/63.221/0.000 ms

================================== Ai Message ==================================

👉 Result:
{'messages': [HumanMessage(content="What's the latency like for `https://langchain.com`?", 
additional_kwargs={}, response_metadata={}, id='138078ec-6b3f-471a-afc8-88ab3d357c21'), 
AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_4t1FqAn89jloj5f20eKUUe3P', 
'function': {'arguments': '{"url":"https://langchain.com","return_error":true}', 'name': 'ping'}, 
'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 
22, 'prompt_tokens': 88, 'total_tokens': 110, 'completion_tokens_details': {'accepted_prediction_tokens': 
0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': 
{'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': 
None, 'id': 'chatcmpl-BkuFAHEE8O7tulT8N8xQQvraKLHho', 'service_tier': 'default', 'finish_reason': 
'tool_calls', 'logprobs': None}, id='run--7166c248-5e6d-4cb0-aa60-e4ada5908728-0', 
tool_calls=[{'name': 'ping', 'args': {'url': 'https://langchain.com', 'return_error': 
True}, 'id': 'call_4t1FqAn89jloj5f20eKUUe3P', 'type': 'tool_call'}], usage_metadata={
'input_tokens': 88, 'output_tokens': 22, 'total_tokens': 110, 'input_token_details': 
{'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}), 
ToolMessage(content='PING langchain.com (99.83.190.102) 56(84) bytes of data.\n64 bytes 
from 99.83.190.102 (99.83.190.102): icmp_seq=1 ttl=63 time=65.6 ms\n\n--- langchain.com 
ping statistics ---\n1 packets transmitted, 1 received, 0% packet loss, time 0ms\nrtt 
min/avg/max/mdev = 65.625/65.625/65.625/0.000 ms\n', name='ping', id='969e7527-e299-497e-965a-e0132344e0cc', 
tool_call_id='call_4t1FqAn89jloj5f20eKUUe3P'), AIMessage(content='The latency for 
`https://langchain.com` is approximately 65.6 ms.', additional_kwargs={'refusal': None}, 
response_metadata={'token_usage': {'completion_tokens': 19, 'prompt_tokens': 226, 
'total_tokens': 245, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 
'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 
'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 
'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-BkuFAngbuUaByP8WqL1vmo35N7ILv', 
'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None}, id='run--3c917e1c-19ff-44db-b931-8f8822cf1aa4-0', 
usage_metadata={'input_tokens': 226, 'output_tokens': 19, 'total_tokens': 245, 'input_token_details': 
{'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}
'''

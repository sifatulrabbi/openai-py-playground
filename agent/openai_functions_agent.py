import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMMathChain
from langchain.agents import initialize_agent, AgentType, Tool


gpt_35_turbo = "gpt-3.5-turbo"

llm = ChatOpenAI(temperature=0, model=gpt_35_turbo)
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)


def middle_man(*args):
    print("args", args)
    return llm_math_chain.run(*args)


tools = [
    Tool(
        name="Calculator",
        func=middle_man,
        description="useful for when you need to answer questions about math",
    ),
]

agent_executor = initialize_agent(
    llm=llm, tools=tools, agent=AgentType.OPENAI_FUNCTIONS, verbose=True
)
"""
This is what happens under the hood:

```
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.tools.render import format_tool_to_openai_function


llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
agent = {
    "input": lambda x: x["input"],
    "agent_scratchpad": lambda x: format_to_openai_functions(x["intermediate_steps"])
} | prompt | llm_with_tools | OpenAIFunctionsAgentOutputParser()

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```
"""

mrlk = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_MULTI_FUNCTIONS,
    verbose=True,
    max_iteration=10,
    early_stopping_method="generate",
)

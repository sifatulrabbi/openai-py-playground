if __name__ == "__main__":
    import openai
    import os
    from dotenv import load_dotenv

    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY", None)

import math
from random import random
from langchain.chat_models import ChatOpenAI
from langchain.agents import tool, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools.render import format_tool_to_openai_function
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.schema import HumanMessage, AIMessage

MEMORY_KEY = "chat_history"


@tool
def get_word_length(word: str):
    """Returns the length of a word"""
    return len(word)


@tool
def send_booking_invitation_to_client(client_email: str, discount_amount: float):
    """Sends a booking invitation to the client's email.

    Args:
        client_email (str): Client's email
        discount_amount (float): Discount amount in float format, i.e. 10% will be 0.01.

    Returns:
        str: Either a success message or the error message.
    """
    if math.floor(random() * 10) < 2:
        return "Failed to send the booking invitation due to network error."
    return "Successfully sent the booking invitation."


def string_to_chat_history_list(msg: str):
    messages = msg.split("\n")
    messages_list = []
    for message in messages:
        if message.startswith("Human: "):
            messages_list.append(HumanMessage(content=message.split("Human: ")[1]))
        if message.startswith("AI: "):
            messages_list.append(AIMessage(content=message.split("AI: ")[1]))
    return messages_list


tools = [
    get_word_length,
    send_booking_invitation_to_client,
]
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are very powerful assistant, but bad at calculating lengths of words.",
        ),
        MessagesPlaceholder(variable_name=MEMORY_KEY),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_functions(
            x["intermediate_steps"]
        ),
        "chat_history": lambda x: string_to_chat_history_list(x["chat_history"]),
    }
    | prompt
    | llm_with_tools
    | OpenAIFunctionsAgentOutputParser()
)
memory = ConversationBufferMemory(memory_key=MEMORY_KEY)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)

try:
    while True:
        msg = input("User: ")
        print(memory.load_memory_variables({"input": msg}))
        result = agent_executor.invoke({"input": msg})
        print("Agent: ", result.get("output"))
except KeyboardInterrupt as e:
    chat_history = []
    print("Gracefully shutting down the Agent.")
    exit()

from dotenv import load_dotenv

load_dotenv()

import os
import openai
from practice_agent.openai_functions_agent import agent_executor as fn_agent
from practice_agent.mem_agents import mem_completion_chain, mem_chat_chain
from practice_agent.qa_bot import qa_bot_with_chroma
from practice_agent.agent_001 import agent_executor

openai.api_key = os.getenv("OPENAI_API_KEY", None)


class Color:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"


def use_fn_agent():
    result = fn_agent.invoke({"input": "What is 5 raise to 2 power?"})
    print("\n", result)


def use_mem_agent():
    llm_chain = mem_completion_chain()
    llm_chain.predict(human_input="Hi I'm Fredrick")
    llm_chain.predict(human_input="Remember this text 'Crows are brown'")
    msg = llm_chain.predict(
        human_input="What is the color of crows based on the text I sent you?"
    )
    print(f"AI: {msg}")


def use_chat_mem_chain():
    chat_llm_chain = mem_chat_chain()
    chat_llm_chain.predict(human_input="Hi, there my friend.")
    msg = chat_llm_chain.predict(human_input="Not too bad - how are you?")
    print(msg)


def use_qa_chroma_bot():
    chain = qa_bot_with_chroma()
    query = "What did the president say about Ketanji Brown Jackson"
    result = chain.run(query)
    print(result)


if __name__ == "__main__":
    while True:
        msg = input(f"{Color.BLUE}User: {Color.BLUE}")
        result = agent_executor.invoke({"input": msg})
        print(f"{Color.BLUE}AI: {result.get('output')}{Color.BLUE}")

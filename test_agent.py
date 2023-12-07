"""
This file is not a part of the project.

This file is only used when testing out the simple-agent.
"""

from configs import AppConfig
from icecream import ic
from portfolio_bot import MultiFunctionsBot
from portfolio_bot.prompts import CustomBotPrompt
from portfolio_bot.tools import BotTools
from portfolio_bot.memory import SemiPersistentChatMemory

AppConfig.prepare()

if __name__ == "__main__":
    print("Hi, I'm X-Agent let me know how I can help you.")
    prompt = CustomBotPrompt()
    tools = BotTools()
    memory = SemiPersistentChatMemory(
        user_id="tests-user-id", memory_key=prompt.MEMORY_KEY
    )
    agent = MultiFunctionsBot(prompt=prompt, tools=tools, memory=memory)
    try:
        # with open("tmp/question.txt", "r") as f:
        #     question = f.read()
        # reply = agent.invoke(
        #     user_msg=f"Will sifatul be a good fit for our job?\n{question}"
        # )
        # print("Agent: ", reply)
        while True:
            msg = input("User: ")
            reply = agent.invoke(msg)
            print("Agent: ", reply)
    except KeyboardInterrupt as e:
        exit()
    except Exception as e:
        ic(e)
        exit()

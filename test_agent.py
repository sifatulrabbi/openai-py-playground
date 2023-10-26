"""
This file is not a part of the project.

This file is only used when testing out the simple-agent.
"""

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY", None)

from portfolio_bot import ReActAgentBot, MultiFunctionsBot
from portfolio_bot.prompts import ReActPrompt, CustomBotPrompt
from portfolio_bot.tools import BotTools
from portfolio_bot.memory import SemiPersistentChatMemory


# test_user_id = "KUawqcXFvJa9Pap4zfrQneEa7hv1"
# test_org_id = "X-BookerTestOrg"

if __name__ == "__main__":
    print("Hi, I'm X-Agent let me know how I can help you.")
    prompt = CustomBotPrompt()
    tools = BotTools()
    memory = SemiPersistentChatMemory(
        user_id="tests-user-id", memory_key=prompt.MEMORY_KEY
    )
    agent = MultiFunctionsBot(prompt=prompt, tools=tools, memory=memory)
    # prompt = ReActPrompt(tools=tools)
    # react_agent = ReActAgentBot(prompt=prompt, tools=tools, memory=memory)
    try:
        while True:
            msg = input("User: ")
            reply = agent.invoke(msg)
            print("Agent: ", reply)
    except KeyboardInterrupt as e:
        exit()

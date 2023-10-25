"""
This file is not a part of the project.

This file is only used when testing out the simple-agent.
"""

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY", None)

from portfolio_bot import (
    MultiFunctionsBot,
    CustomBotPrompt,
    SemiPersistentChatMemory,
    XAgentTools,
)


test_user_id = "KUawqcXFvJa9Pap4zfrQneEa7hv1"
test_org_id = "X-BookerTestOrg"

if __name__ == "__main__":
    print("Hi, I'm X-Agent let me know how I can help you.")
    prompt = CustomBotPrompt(
        user_name="Sifatul",
        user_email="s.rabbi@milogistix.uk",
        user_role="admin",
        organization_id=test_org_id,
        organization_name="X-Booker Demo",
    )
    memory = SemiPersistentChatMemory(
        user_id=test_user_id, memory_key=prompt.MEMORY_KEY
    )
    tools = XAgentTools(user_id=test_user_id, org_id=test_org_id)
    agent = MultiFunctionsBot(prompt=prompt, tools=tools, memory=memory)
    try:
        while True:
            msg = input("User: ")
            reply = agent.invoke(msg)
            print("Agent: ", reply)
    except KeyboardInterrupt as e:
        exit()

import os
import sys
from configs import AppConfig
from icecream import ic

parent_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(parent_dir)

AppConfig.prepare()

import unittest
from portfolio_bot.portfolio_bot_core import MultiFunctionsBot
from portfolio_bot.prompts.customized_user_prompt import CustomBotPrompt
from portfolio_bot.tools import BotTools
from portfolio_bot.memory import SemiPersistentChatMemory


class SendEmailTest(unittest.IsolatedAsyncioTestCase):
    async def test_send_emails(self):
        try:
            prompt = CustomBotPrompt()
            tools = BotTools()
            memory = SemiPersistentChatMemory(
                memory_key=prompt.MEMORY_KEY, user_id="test_user"
            )
            agent = MultiFunctionsBot(prompt=prompt, tools=tools, memory=memory)
            reply = agent.invoke(
                user_msg="I'm John Cornor, my email is john.cornor@example.com. Send sifatul an email so that he can reply back to me with his pricing."
            )
            ic(reply)
        except Exception as e:
            ic(e)
            self.fail(str(e))

if __name__ == "__main__":
    unittest.main()

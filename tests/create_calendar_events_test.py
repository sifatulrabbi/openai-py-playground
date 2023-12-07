import os
import sys
from configs import AppConfig

parent_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(parent_dir)

AppConfig.prepare()

import unittest
from portfolio_bot.portfolio_bot_core import MultiFunctionsBot
from portfolio_bot.prompts.customized_user_prompt import CustomBotPrompt
from portfolio_bot.tools import BotTools
from portfolio_bot.memory import SemiPersistentChatMemory


class CreateCalendarEventTest(unittest.IsolatedAsyncioTestCase):
    def test_create_calendar_event(self):
        prompt = CustomBotPrompt()
        tools = BotTools()
        memory = SemiPersistentChatMemory(
            memory_key=prompt.MEMORY_KEY, user_id="test_user"
        )
        agent = MultiFunctionsBot(prompt=prompt, tools=tools, memory=memory)
        self.fail("test is not setup yet")


if __name__ == "__main__":
    unittest.main()

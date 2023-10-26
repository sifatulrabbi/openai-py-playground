from typing import Any, Dict
from langchain.prompts.chat import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.format_scratchpad import format_to_openai_functions

from .prompt import BotPrompt
from ..memory import string_to_chat_history_list


class CustomBotPrompt(BotPrompt):
    """Customized user prompt to use with XAgent."""

    def __init__(self):
        self.MEMORY_KEY = "chat_history"
        """The key where the chat_history will load."""
        self.USER_INPUT_KEY = "input"
        """The key where the user message will load."""
        self.INTERMEDIATE_STEPS_KEY = "agent_scratchpad"
        """The key where the intermediate step will load."""
        with open("prompts/portfolio.txt", "r") as f:
            content = f.read()
        self._template = content

    @property
    def chat_prompt(self) -> ChatPromptTemplate:
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self._template),
                MessagesPlaceholder(variable_name=self.MEMORY_KEY),
                ("human", "{input}"),
                MessagesPlaceholder(variable_name=self.INTERMEDIATE_STEPS_KEY),
            ]
        )
        return prompt

    @property
    def initial_steps(self) -> Dict[str, Any]:
        return {
            "input": lambda x: x.get("input"),
            "chat_history": lambda x: string_to_chat_history_list(
                x.get("chat_history")
            ),
            "agent_scratchpad": lambda x: self._openai_func_parser(x),
        }

    def _openai_func_parser(self, x: Any):
        res = format_to_openai_functions(intermediate_steps=x.get("intermediate_steps"))
        for r in res:
            print(r.json())
        return res

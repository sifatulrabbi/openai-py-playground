from langchain import hub
from langchain.tools.render import render_text_description
from langchain.prompts.chat import ChatPromptTemplate
from langchain.agents.format_scratchpad import format_log_to_messages
from typing import Dict, Any, List

from .prompt import BotPrompt
from ..tools import BotTools
from ..memory import string_to_chat_history_list

TEMPLATE_TOOL_RESPONSE = """TOOL RESPONSE: 
---------------------
{observation}

USER'S INPUT
--------------------

Okay, so what is the response to my last comment? If using information obtained from the tools you must mention it explicitly without mentioning the tool names - I have forgotten all TOOL RESPONSES! Remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else - even if you just want to respond to the user. Do NOT respond with anything except a JSON snippet no matter what!"""


class ReActPrompt(BotPrompt):
    def __init__(self, tools: BotTools):
        self.MEMORY_KEY = "chat_history"
        self._prompt = hub.pull("hwchase17/react-chat-json")
        self._prompt = self._prompt.partial(
            tools=render_text_description(tools.tools_list),
            tool_names=", ".join([t.name for t in tools.tools_list]),
        )

    @property
    def chat_prompt(self) -> ChatPromptTemplate:
        return self._prompt

    @property
    def initial_steps(self) -> Dict[str, Any]:
        return {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_log_to_messages(
                x["intermediate_steps"],
                template_tool_response=TEMPLATE_TOOL_RESPONSE,
            ),
            "chat_history": lambda x: self._parse_chat_history(x),
        }

    def _parse_chat_history(self, data) -> List:
        chat_history = data.get(self.MEMORY_KEY)
        if chat_history:
            if isinstance(chat_history, str):
                return string_to_chat_history_list(chat_history)
            return data.get(self.MEMORY_KEY)
        return []

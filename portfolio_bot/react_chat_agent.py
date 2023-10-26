from langchain.agents import AgentExecutor
from langchain.agents.output_parsers import JSONAgentOutputParser
from langchain.chat_models import ChatOpenAI
from typing import Optional

from .portfolio_bot_core import PortfolioBot
from .prompts import BotPrompt
from .tools import BotTools
from .memory import BotMemory


class ReActAgentBot(PortfolioBot):
    def __init__(
        self,
        *,
        prompt: BotPrompt,
        tools: BotTools,
        memory: Optional[BotMemory] = None,
    ):
        self._prompt = prompt
        self._tools = tools
        self._memory = memory
        self._llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
        self._llm = self._llm.bind(stop=["\nObservation"])
        self._agent = (
            self._prompt.initial_steps
            | self._prompt.chat_prompt
            | self._llm
            | JSONAgentOutputParser()
        )
        self._executor = AgentExecutor(
            agent=self._agent,
            tools=self._tools.tools_list,
            memory=self._memory.memory,
            handle_parsing_errors=True,
            verbose=True,
        )

    @property
    def executor(self) -> AgentExecutor:
        return self._executor

    def invoke(self, user_msg: str) -> str:
        result = self._executor.invoke({"input": user_msg})
        return result.get("output")

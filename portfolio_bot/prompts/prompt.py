from abc import ABC, abstractproperty
from langchain.prompts.chat import ChatPromptTemplate
from typing import Dict, Any


class BotPrompt(ABC):
    @abstractproperty
    def chat_prompt(self) -> ChatPromptTemplate:
        pass

    @abstractproperty
    def initial_steps(self) -> Dict[str, Any]:
        pass

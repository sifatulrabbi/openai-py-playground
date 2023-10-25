from abc import ABC, abstractproperty
from langchain.prompts.chat import ChatPromptTemplate


class BotPrompt(ABC):
    @abstractproperty
    def chat_prompt(self) -> ChatPromptTemplate:
        pass

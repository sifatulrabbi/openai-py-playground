from abc import ABC, abstractproperty
from langchain.memory.chat_memory import BaseChatMemory


class BotMemory(ABC):
    @abstractproperty
    def memory(self) -> BaseChatMemory:
        pass

from abc import ABC, abstractproperty, abstractmethod
from typing import Any


class XAgentTool(ABC):
    @abstractproperty
    def name(self) -> str:
        pass

    @abstractproperty
    def description(self) -> str:
        pass

    @abstractmethod
    def tool_func(self, *args) -> Any:
        pass

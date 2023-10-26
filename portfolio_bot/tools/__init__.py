"""
All the tools for the Agent to perform different tasks based on the user's request.
"""

from typing import List
from langchain.tools import Tool, BaseTool
from langchain.tools.render import format_tool_to_openai_function

from .tool import BotTool
from .send_email import SendEmail


class BotTools:
    """Agent tools orchestrator."""

    def __init__(self):
        """Initialize the Agent Tools."""
        self._available_tools: List[BotTool] = [
            SendEmail(),
        ]

    @property
    def openai_functions(self):
        functions = [format_tool_to_openai_function(t) for t in self.tools_list]
        return functions

    @property
    def tools_list(self) -> List[BaseTool]:
        """Get the available tools list.

        Returns:
            List[Tool]: List of `langchain.tools.BaseTool`
        """
        tools: List[BaseTool] = []
        for tool in self._available_tools:
            tools.append(
                Tool.from_function(
                    func=tool.tool_func, name=tool.name, description=tool.description
                )
            )
        return tools

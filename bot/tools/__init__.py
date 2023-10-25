"""
All the tools for the Agent to perform different tasks based on the user's request.
"""

from typing import List
from langchain.tools import Tool
from langchain.tools.render import format_tool_to_openai_function

from .xagent_tool import XAgentTool


class XAgentTools:
    """Agent tools orchestrator."""

    def __init__(self, *, user_id: str, org_id: str):
        """Initialize the Agent Tools.

        Args:
            user_id (str): The user's ID.
            org_id (str): The user's organization ID.
        """
        if not user_id or not org_id:
            raise ValueError(
                "`user_id` and `org_id` is required to instantiate the tools"
            )
        self._user_id = user_id
        self._org_id = org_id
        self._available_tools: List[XAgentTool] = []

    @property
    def openai_functions(self):
        functions = [format_tool_to_openai_function(t) for t in self.tools_list]
        return functions

    @property
    def tools_list(self) -> List[Tool]:
        """Get the available tools list.

        Returns:
            List[Tool]: List of `langchain.tools.Tool`
        """
        tools: List[Tool] = []
        for tool in self._available_tools:
            tools.append(
                Tool(name=tool.name, description=tool.description, func=tool.tool_func)
            )
        return tools

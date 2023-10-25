from langchain.prompts.chat import ChatPromptTemplate, MessagesPlaceholder
from .prompt import BotPrompt

# TODO: update this test prompt for the portfolio bot.
prompt_template = """You are a helpful agent who supports the users with managing their business. You will send booking invitations or booking links to the user's client emails with or without discounts. You will also help them with querying booking requests submitted to their organization, and also with querying their todo list using the tools provided to you. If you think the user did not provided enough information to complete a task or query then you will ask them to provide those information.

When you send booking information or todo list information to the user make sure to format it with Markdown syntax to make the data more human readable.

Following are the information of the current user and their organization. Use these information wisely with the provided tools.
User's fullname: {user_name}
User's email address{user_email}
User's role in the organization: {user_role}
User's organization id: {organization_id}
User's organization name: {organization_name}
"""


class CustomBotPrompt(BotPrompt):
    """Customized user prompt to use with XAgent."""

    def __init__(
        self,
        user_name: str,
        user_email: str,
        user_role: str,
        organization_id: str,
        organization_name: str,
    ):
        self.MEMORY_KEY = "chat_history"
        """The key where the chat_history will load."""
        self.USER_INPUT_KEY = "input"
        """The key where the user message will load."""
        self.INTERMEDIATE_STEPS_KEY = "agent_scratchpad"
        """The key where the intermediate step will load."""
        self._template = prompt_template.format(
            user_name=user_name,
            user_email=user_email,
            user_role=user_role,
            organization_id=organization_id,
            organization_name=organization_name,
        )

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

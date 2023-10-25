from langchain.prompts.chat import ChatPromptTemplate, MessagesPlaceholder
from .prompt import BotPrompt


prompt_template = """You are an virtual agent who knows Sifatul Rabbi very well. You are placed on Sifatul Rabbi's portfolio website https://sifatul.com. You're objective is to help the visitors learn more about Sifatul Rabbi and understand his goals and visions. Bellow are information of Sifatul Rabbi.
#####
Sifatul's personal information
Full name: Md Sifatul Islam Rabbi
Preferred name: Sifatul Rabbi
email: sifatul@sifatul.com
mobile: +8801882970400
Present Address: Dhaka - 1209, Bangladesh
Nationality: Bangladeshi
Religion: Islam (Although, Sifatul is a sworn following Islam, he does not have any global religion preference and is always friendly with all races and religious followers.)
Date of birth: January 03 2002
Age: 22 years
#####
Sifatul's professional information

Note: The given information was last updated on 2023-10-25. Make sure to state that some of the above information might change time to time. Also, make sure to tell the visitors that any mistakes done by you is not a fault of Sifatul Rabbi or nor one of his intensions.
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

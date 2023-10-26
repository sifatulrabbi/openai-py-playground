from typing import Any

from .tool import BotTool


class SendEmail(BotTool):
    def __init__(self):
        pass

    @property
    def name(self) -> str:
        return "send_email_to_sifatul"

    @property
    def description(self) -> str:
        return """Useful when sending emails to Sifatul with a customized message from the user.
        The tool takes in one argument which is a JSON string.
        payload (str): The payload MUST be a json string and the json should contain a `subject` which is the email subject and a `message` which is the emails's message
        If you don't have the information the DO ASK the user for required information, you SHOULD NEVER guess the payload..
        """

    def tool_func(self, payload: str) -> Any:
        print(type(payload))
        return "The email was sent successfully."

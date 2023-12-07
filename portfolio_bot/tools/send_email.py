import httpx
import json
from typing import Any, Dict
from icecream import ic
from configs import AppConfig
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
        payload (str): The payload MUST be a json string and the json should contain a `subject` which is the email subject, a `message` which is the emails's message, and a `reply_email` the email of the sender who wants to connect with sifatul.
        If you don't have the information then DO ASK the user for required information, you SHOULD NEVER guess the payload.
        """

    def tool_func(self, payload: Dict[str, str]) -> Any:
        """Useful when sending emails to sifatul on behalf of the website visitor.

        Args:
            payload (Dict[str, str]): This payload should have `subject`, `message`, and the `reply_email` where sifatul can send his replies.
        Returns:
            str: The success message or the error message."""
        if isinstance(payload, str):
            payload = json.loads(payload)

        if not payload.get("reply_email"):
            return "`reply_email` is not present in the payload please ask for an email from the sender where sifatul can send his replies."

        if not payload.get("message"):
            return "`message` is not found in the payload please ask to the use for the message they want to send to sifatul"

        if not payload.get("subject"):
            return "`subject` is not found in the payload please ask to the use for the subject of their email"

        try:
            if not AppConfig.SIFATUL_API_URL:
                raise EnvironmentError("SIFATUL_API_URL env is not found")

            res = httpx.post(
                url=AppConfig.SIFATUL_API_URL,
                json={
                    "message": payload.get("message"),
                    "reply_to": payload.get("reply_email"),
                    "subject": payload.get("subject"),
                },
            )

            if res.status_code != httpx.codes.OK:
                raise Exception(res.json().get("message"))
            return "Email sent successfully"
        except Exception as e:
            ic(e)
            return f"unable to send the email, error: {str(e)}"

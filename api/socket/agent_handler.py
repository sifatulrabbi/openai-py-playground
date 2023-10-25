from socketio import AsyncServer
from typing import Dict

from .default_handler import SocketHandler


class AgentSioHandler(SocketHandler):
    def __init__(self, sio: AsyncServer):
        self._sio = sio

    def prepare_handlers(self):
        self._sio.on("chat_message", self._on_chat_message)

    def _on_chat_message(self, sid: str, environ: Dict[str, str]):
        print(f"message: {environ.get('message')}")

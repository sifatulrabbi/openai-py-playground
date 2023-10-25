from abc import ABC, abstractmethod
from socketio import AsyncServer
from typing import Any


class SocketHandler(ABC):
    @abstractmethod
    def prepare_handlers(self):
        pass


class DefaultSioHandlers(SocketHandler):
    """Default socket handlers."""

    def __init__(self, sio: AsyncServer):
        self._sio = sio

    def prepare_handlers(self):
        self._sio.on("connect", self._on_connect)
        self._sio.on("disconnect", self._on_disconnect)

    def _on_connect(self, sid: str, environ: Any):
        print(f"client connected: {sid}")

    def _on_disconnect(self, sid: str):
        print(f"client disconnected: {sid}")

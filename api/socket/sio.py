from socketio import AsyncServer
from configs import PY_ENV


sio = AsyncServer(
    async_mode="asgi",
    async_handlers=True,
    logger=PY_ENV == "development",
    always_connect=False,
)

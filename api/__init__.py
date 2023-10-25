from socketio import ASGIApp

from .api import api
from .socket import sio


app = ASGIApp(sio, api)

#! /usr/bin/python3

import os
import uvicorn
import openai
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv("PORT", "8001")
PY_ENV = os.getenv("PY_ENV", "development")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)

openai.api_key = OPENAI_API_KEY

host = "127.0.0.1"
ex_dirs = [".*", "cache", "tmp", "docs"]
log_level = "info" if PY_ENV == "production" else "debug"
reload = False if PY_ENV == "production" else True
workers = 5

if __name__ == "__main__":
    uvicorn.run(
        app="api:app",
        host=host,
        port=int(PORT),
        reload_excludes=ex_dirs,
        reload=reload,
        workers=None if reload else workers,
    )

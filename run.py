#! /usr/bin/python3

import uvicorn
from configs import AppConfig

AppConfig.prepare()

host = "127.0.0.1"
ex_dirs = [".*", "cache", "tmp", "docs"]
log_level = "info" if AppConfig.PY_ENV == "production" else "debug"
reload = False if AppConfig.PY_ENV == "production" else True
workers = 5

if __name__ == "__main__":
    uvicorn.run(
        app="api:app",
        host=host,
        port=int(AppConfig.PORT),
        reload_excludes=ex_dirs,
        reload=reload,
        workers=None if reload else workers,
    )

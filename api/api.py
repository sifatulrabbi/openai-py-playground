from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Optional


api = FastAPI(debug=True, title="portfolio-bot", version="0.1.0")


@api.get("/health")
async def get_health_info(message: Optional[str] = None):
    return JSONResponse(
        status_code=200,
        content={
            "message": message,
            "reply": "The API is working fine.",
        },
    )

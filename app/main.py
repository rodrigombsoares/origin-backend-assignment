import uvicorn
from fastapi import Depends, FastAPI

from app.controllers import router

app = FastAPI(
    title="Origin Backend",
    description="Project designed as Origin's take-home assignment",
    version="1.0.0",
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

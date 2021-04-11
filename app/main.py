import uvicorn
from fastapi import Depends, FastAPI

from controllers import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

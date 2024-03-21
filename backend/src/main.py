from fastapi import FastAPI
import uvicorn
from .api_v1.applications import router
from . import models
from .database import engine

app = FastAPI()
app.include_router(router.router)
models.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

from fastapi import FastAPI
from .api_v1.applications import router
from . import models
from .database import engine

app = FastAPI()
app.include_router(router.router)
models.Base.metadata.create_all(bind=engine)


@app.get('/')
def hello():
    return 'Hello'

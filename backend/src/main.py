from fastapi import FastAPI
from .api_v1.applications import router as application_router
from .api_v1.workplace import router as workplace_router
from . import models
from .database import engine

app = FastAPI()
app.include_router(application_router.router)
app.include_router(workplace_router.router)
models.Base.metadata.create_all(bind=engine)


@app.get('/')
def hello():
    return 'Hello'
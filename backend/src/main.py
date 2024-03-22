from fastapi import FastAPI
import uvicorn
from api_v1.applications.router import router_application
from api_v1.profession.router import router_profession
from api_v1.new_vacancy.router import router_vacancy
from . import models
from .database import engine

app = FastAPI()
app.include_router(router_application)
app.include_router(router_profession)
app.include_router(router_vacancy)
models.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

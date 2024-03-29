from fastapi import FastAPI
import uvicorn

from .api_v1.applications import router as application_router
from .api_v1.about_vacancy import router as workplace_router
from .api_v1.new_vacancy import router as vacancy_router
from .api_v1.profession import router as vacancy_profession
from . import models
from .database import engine


app = FastAPI(
    title='HRSpace',
    summary='A builder for finding recruiters',
    version='0.0.1',
    license_info={
        'name': 'HRSpace',
        'url': 'https://HRSpace.ru/',
    }
)


app.include_router(application_router.router)
app.include_router(vacancy_router.router)
app.include_router(vacancy_profession.router)
app.include_router(workplace_router.router)

models.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

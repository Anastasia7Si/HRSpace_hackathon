from fastapi import FastAPI

import uvicorn

from api_v1.app.views import router

app = FastAPI(
    title='HRSpace',
    summary='A builder for finding recruiters',
    version='0.0.1',
    license_info={
        'name': 'HRSpace',
        'url': 'https://HRSpace.ru/',
    }
)
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

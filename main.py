from fastapi import FastAPI

import uvicorn

from api_v1.app.views import get_profession_id

app = FastAPI()
app.include_router(get_profession_id)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

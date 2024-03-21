from pydantic import BaseModel


class BaseApplication(BaseModel):
    title: str
    is_published: bool

    class Config:
        orm_mode = True


class CreateApplication(BaseApplication):
    class Config:
        orm_mode = True

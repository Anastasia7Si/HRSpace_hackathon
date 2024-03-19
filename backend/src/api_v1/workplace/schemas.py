from pydantic import BaseModel


class City(BaseModel):

    region: str
    city: str


class Metro(BaseModel):

    city: str
    metro: str

from pydantic import BaseModel


class CityCreate(BaseModel):

    region: str
    city: str

    class Config:
        orm_mode = True


class CityGet(CityCreate):

    id: int

    class Config:
        orm_mode = True


class TimezoneCreate(BaseModel):

    title: str

    class Config:
        orm_mode = True


class MetroCreate(BaseModel):

    city_id: int
    metro: str

    class Config:
        orm_mode = True


class MetroGet(MetroCreate):

    id: int

    class Config:
        orm_mode = True


class CityWithMetro(CityCreate):

    metro: list[MetroGet]

    class Config:
        orm_mode = True

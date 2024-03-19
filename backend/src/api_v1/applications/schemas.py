from pydantic import BaseModel
from typing import List, Optional
from ..workplace.schemas import CityCreate


class ApplicationDTO(BaseModel):
    title: str
    application_cities: list[CityCreate]

    class Config:
        orm_mode = True


class ApplicationCreate(BaseModel):
    title: str
    city_ids: list[int]

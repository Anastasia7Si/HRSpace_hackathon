from pydantic import BaseModel, Field
from typing import List, Optional
from ..about_vacancy.schemas import CityCreate, TimezoneCreate


class ApplicationDTO(BaseModel):
    title: str
    city: CityCreate
    relocation: bool
    remote_work: bool
    timezone_from: TimezoneCreate
    timezone_to: TimezoneCreate

    class Config:
        orm_mode = True


class ApplicationCreate(BaseModel):
    title: str
    city_id: int
    relocation: bool = Field(default=False)
    remote_work: bool = Field(default=False)
    timezone_from_id: Optional[int]
    timezone_to_id: Optional[int]

    class Config:
        orm_mode = True

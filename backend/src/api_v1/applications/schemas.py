from pydantic import BaseModel, Field

from typing import Optional
from ..about_vacancy.schemas import CityCreate, TimezoneCreate


class ApplicationDTO(BaseModel):
    title: str
    city: CityCreate
    relocation: bool
    remote_work: bool
    timezone_from: Optional[TimezoneCreate]
    timezone_to: Optional[TimezoneCreate]

    class Config:
        orm_mode = True


class ApplicationCreate(BaseModel):
    title: str
    city_id: int
    metro_id: int
    relocation: bool = Field(default=False)
    remote_work: bool = Field(default=False)
    timezone_from_id: Optional[int] = Field(default=None, allow_none=True)
    timezone_to_id: Optional[int] = Field(default=None, allow_none=True)

    class Config:
        orm_mode = True

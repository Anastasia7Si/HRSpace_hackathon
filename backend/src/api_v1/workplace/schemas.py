from pydantic import BaseModel
from typing import List


class CityCreate(BaseModel):

    region: str
    city: str

    class Config:
        orm_mode = True


# class Metro(BaseModel):
#
#     city: str
#     metro: str
#
#     class Config:
#         orm_mode = True

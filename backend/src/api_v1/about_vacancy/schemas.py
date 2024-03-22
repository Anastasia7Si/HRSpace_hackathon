from pydantic import BaseModel


class CityCreate(BaseModel):

    region: str
    city: str

    class Config:
        orm_mode = True


class TimezoneCreate(BaseModel):

    title: str

    class Config:
        orm_mode = True


# class Metro(BaseModel):
#
#     city: str
#     metro: str
#
#     class Config:
#         orm_mode = True

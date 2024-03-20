from sqlalchemy import select
from fastapi import Depends, status, Query
from sqlalchemy.orm import Session
from ... import models
from . import schemas
from fastapi import APIRouter
from ...database import get_db
from fastapi_filter.contrib.sqlalchemy import Filter
from fastapi_filter import FilterDepends
from typing import Optional, List

router = APIRouter(
    prefix='/workplace',
    tags=['Workplace']
)


# class CityFilter(Filter):
#
#     class Constants(Filter.Constants):
#         model = models.City
#         search_model_fields = ["region", "city"]


# @router.get('/city', response_model=None)
# def get_city(db: Session = Depends(get_db))
#
#     city = db.query(models.CityOrm).all()
#
#     return city


@router.get('/city', response_model=None)
def get_city(db: Session = Depends(get_db), search: str = Query(None, description="Поисковый запрос")):
    query = db.query(models.CityOrm)
    if search:
        query = query.filter(models.CityOrm.city.like(f"%{search}%"))
        # Здесь можно добавить другие поля модели для поиска по аналогии с Django

    cities = query.all()
    return cities


@router.post('/city', status_code=status.HTTP_201_CREATED, response_model=None)
def add_city(city_create: schemas.CityCreate, db: Session = Depends(get_db)):
    new_city = models.CityOrm(**city_create.dict())
    db.add(new_city)
    db.commit()
    db.refresh(new_city)

    return new_city


# @router.get('/metro', response_model=None)
# def get_metro(db: Session = Depends(get_db)):
#     metro = db.query(models.MetroOrm).all()
#
#     return metro
#
#
# @router.post('/metro', status_code=status.HTTP_201_CREATED, response_model=None)
# def add_metro(metro_create: schemas.Metro, db: Session = Depends(get_db)):
#     new_metro = models.MetroOrm(**metro_create.dict())
#     db.add(new_metro)
#     db.commit()
#     db.refresh(new_metro)
#
#     return new_metro

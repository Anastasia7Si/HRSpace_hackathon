from typing import List
from fastapi import Depends, status
from sqlalchemy.orm import Session
from ... import models
from . import schemas
from fastapi import APIRouter
from ...database import get_db
from fastapi_filter.contrib.sqlalchemy import Filter
from fastapi_filter import FilterDepends

router = APIRouter(
    prefix='/workplace',
    tags=['Workplace']
)


class CityFilter(Filter):
    class Constants(Filter.Constants):
        model = models.City
        search_model_fields = ["region", "city"]


@router.get('/city', response_model=None)
async def get_city(
        city_filter: CityFilter = FilterDepends(CityFilter),
        db: Session = Depends(get_db)
):
    query = select(City)
    query = city_filter.sort(query)
    result = await db.execute(query)

    return result.scalars.all()

    # city = db.query(models.City).all()

    # return city


@router.post('/city', status_code=status.HTTP_201_CREATED, response_model=List[schemas.City])
def create_workplace(city_create: schemas.City, db: Session = Depends(get_db)):
    new_city = models.City(**city_create.dict())
    db.add(new_city)
    db.commit()
    db.refresh(new_city)

    return new_city


@router.get('/metro', response_model=None)
def get_metro(db: Session = Depends(get_db)):
    metro = db.query(models.Metro).all()

    return metro


@router.post('/metro', status_code=status.HTTP_201_CREATED, response_model=List[schemas.Metro])
def create_workplace(metro_create: schemas.City, db: Session = Depends(get_db)):
    new_metro = models.Metro(**metro_create.dict())
    db.add(new_metro)
    db.commit()
    db.refresh(new_metro)

    return new_metro

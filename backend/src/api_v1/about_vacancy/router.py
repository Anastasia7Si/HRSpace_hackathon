from fastapi import Depends, status, Query
from sqlalchemy.orm import Session
from ... import models
from . import schemas
from fastapi import APIRouter
from ...database import get_db

router = APIRouter(
    prefix='/vacancy',
    tags=['Vacancy']
)


@router.get('/city', response_model=list[schemas.CityGet])
def get_city(db: Session = Depends(get_db), search: str = Query(None, description="Поисковый запрос")):
    query = db.query(models.CityOrm)
    if search:
        query = query.filter(models.CityOrm.city.like(f"%{search}%"))
        # Здесь можно добавить другие поля модели для поиска по аналогии с Django

    cities = query.all()
    return cities


@router.get('/citywithmetro', response_model=list[schemas.CityWithMetro])
def get_city(db: Session = Depends(get_db)):
    cities = db.query(models.CityOrm).all()
    return cities


@router.post('/city', status_code=status.HTTP_201_CREATED, response_model=schemas.CityGet)
def add_city(city_create: schemas.CityCreate, db: Session = Depends(get_db)):
    new_city = models.CityOrm(**city_create.dict())
    db.add(new_city)
    db.commit()
    db.refresh(new_city)

    return new_city


@router.get('/timezone', response_model=None)
def get_timezone(db: Session = Depends(get_db)):
    timezones = db.query(models.Timezone).all()
    return timezones


@router.post('/timezone', status_code=status.HTTP_201_CREATED, response_model=None)
def add_timezone(timezone_create: schemas.TimezoneCreate, db: Session = Depends(get_db)):
    new_timezone = models.Timezone(**timezone_create.dict())
    db.add(new_timezone)
    db.commit()
    db.refresh(new_timezone)

    return new_timezone


@router.get('/city/{city_id}/metro', response_model=list[schemas.MetroGet])
def get_metro(city_id: int, db: Session = Depends(get_db)):
    metro = db.query(models.MetroOrm).filter(models.MetroOrm.city_id == city_id).all()

    return metro


@router.post('/metro', status_code=status.HTTP_201_CREATED, response_model=None)
def add_metro(metro_create: schemas.MetroCreate, db: Session = Depends(get_db)):
    new_metro = models.MetroOrm(**metro_create.dict())
    db.add(new_metro)
    db.commit()
    db.refresh(new_metro)
    return new_metro

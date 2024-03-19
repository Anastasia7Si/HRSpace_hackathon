from typing import List
from fastapi import Depends, status
from sqlalchemy.orm import Session, joinedload
from ... import models
from . import schemas
from fastapi import APIRouter
from ...database import get_db
from fastapi import HTTPException


router = APIRouter(
    prefix='/applications',
    tags=['Applications']
)


@router.get('/', response_model=list[schemas.ApplicationDTO])
def test_application(db: Session = Depends(get_db)):
    application = db.query(models.ApplicationOrm).all()

    return application


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ApplicationDTO)
def create_application(application_create: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    cities = []
    for city_id in application_create.city_ids:
        city = db.query(models.CityOrm).filter(models.CityOrm.id == city_id).first()
        if city is None:
                raise HTTPException(status_code=404, detail=f"City with id {city_id} not found")
        cities.append(city)
    new_application = models.ApplicationOrm(title=application_create.title, application_cities=cities)
    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return new_application

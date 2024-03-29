from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from backend.src import models
from backend.src.database import get_db
from . import schemas

router = APIRouter(
    prefix='/applications',
    tags=['Applications']
)


@router.get('/', response_model=list[schemas.ApplicationDTO])
def test_application(db: Session = Depends(get_db)):
    applications = db.query(models.ApplicationOrm).all()

    return applications


@router.post('/', status_code=status.HTTP_201_CREATED,
             response_model=schemas.ApplicationDTO)
def create_application(application_create: schemas.ApplicationCreate,
                       db: Session = Depends(get_db)):

    new_application = models.ApplicationOrm(**application_create.model_dump())
    city = db.query(models.CityOrm).get(new_application.city_id)
    metro = db.query(models.MetroOrm).get(new_application.metro_id)
    if city.id != metro.city_id:
        raise HTTPException(
            status_code=400,
            detail='В данном городе нет станции метро с указанным ID.'
            )
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    return new_application

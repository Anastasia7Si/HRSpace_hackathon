from typing import List
from fastapi import Depends, status
from sqlalchemy.orm import Session
from ... import models
from . import schemas
from fastapi import APIRouter
from ...database import get_db

router = APIRouter(
    prefix='/applications',
    tags=['Applications']
)


@router.get('/', response_model=None)
def test_application(db: Session = Depends(get_db)):
    application = db.query(models.Application).all()

    return application


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreateApplication])
def create_application(application_create: schemas.CreateApplication, db: Session = Depends(get_db)):
    new_application = models.Application(**application_create.dict())
    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return [new_application]

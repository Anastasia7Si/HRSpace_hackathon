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


@router.get('/', response_model=list[schemas.ApplicationDTO])
def test_application(db: Session = Depends(get_db)):
    applications = db.query(models.ApplicationOrm).all()

    return applications


@router.post('/', status_code=status.HTTP_201_CREATED,
             response_model=schemas.ApplicationDTO)
def create_application(application_create: schemas.ApplicationCreate,
                       db: Session = Depends(get_db)):
    new_application = models.ApplicationOrm(**application_create.dict())
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    return new_application

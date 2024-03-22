from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...database import get_db
from .schemas import (
    EducationSchemas,
    EmploeyExperienceSchemas,
    WorkerRequirementsSchemas,
    WorkerSchemas,
    WorkerSkills
)
from ... import models

router_vacancy = APIRouter(
    prefix='new_applications',
    tags='New Applications'
)


@router_vacancy.get('/{id_experience}/', response_model=list(EmploeyExperienceSchemas))
def get_worker_experience(id_experience: int, db: Session = Depends(get_db)):
    return db.query(
        models.WorkerExperience
    ).filter(id_experience=id_experience).all()


@router_vacancy.get('/{id_education}/', response_model=list(EducationSchemas))
def get_worker_education(id_education: int, db: Session = Depends(get_db)):
    return db.query(
        models.WorkerEducation
    ).filter(id_education=id_education).all()


@router_vacancy.get('/{id_skills}/', response_model=list(WorkerSkills))
def get_worker_skills(id_skills: id, db: Session = Depends(get_db)):
    return db.query(
        models.WorkerSlills
    ).filter(id_skills=id_skills).all()

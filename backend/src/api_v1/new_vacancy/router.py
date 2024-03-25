from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...database import get_db
from .schemas import (
    EducationSchemas,
    EmployeeExperienceSchemas,
    WorkerSkills,
    AboutEmployerSchemas,
    DescriptionSchemas,
)
from ... import models

router = APIRouter(
    prefix='/new_applications',
    tags=['New Applications']
)


@router.get('/{id_experience}/',
            response_model=list[EmployeeExperienceSchemas])
def get_worker_experience(id_experience: int, db: Session = Depends(get_db)):
    return db.query(
        models.WorkerExperience
    ).filter(models.WorkerExperience.id == id_experience).all()


@router.get('/{id_education}/', response_model=list[EducationSchemas])
def get_worker_education(id_education: int, db: Session = Depends(get_db)):
    return db.query(
        models.WorkerEducation
    ).filter(models.WorkerEducation.id == id_education).all()


@router.get('/{id_skills}/', response_model=list[WorkerSkills])
def get_worker_skills(id_skills: int, db: Session = Depends(get_db)):
    return db.query(
        models.WorkerSkills
    ).filter(models.WorkerSkills.id == id_skills).all()


@router.get('/aboute_employer', response_model=AboutEmployerSchemas)
def get_aboute_emploer(db: Session = Depends(get_db)):
    return db.query(models.AboutEmployer).all()


@router.get(
    "/descriptions/",
    response_model=DescriptionSchemas
)
def get_descriptions(application_id: int, db: Session = Depends(get_db)):
    application = db.query(models.ApplicationOrm).filter(
        models.ApplicationOrm.id == application_id).all()
    return {
        "additional_conditions": application.description_emploey,
        "bonuses": application.employee_requirements,
    }


@router.get("/applications/")
def get_application(db: Session = Depends(get_db)):

    application = db.query(models.ApplicationOrm).all()
    return {
        "additional_conditions": application.additional_conditions,
        "bonuses": application.bonuses,
    }

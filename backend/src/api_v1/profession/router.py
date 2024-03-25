from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.src import models
from backend.src.database import get_db
from .schemas import ProfessionSchemas

router = APIRouter(
    prefix='/professions',
    tags=['profession']
)


@router.get('/{profession_id}/', response_model=ProfessionSchemas)
def get_professions(profession_id: int, db: Session = Depends(get_db)):
    result = db.query(
        models.Profession
    ).filter(models.Profession.id == profession_id).all()
    if result is None:
        raise HTTPException(
            f'Выбранной {result} профессие нет в списке, выберете другую!'
        )
    return result

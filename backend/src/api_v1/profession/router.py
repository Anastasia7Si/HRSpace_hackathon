from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from .schemas import ProfessionSchemas
from ...database import get_db
from ... import models

router_profession = APIRouter(
    prefix='professions',
    tags='profession',
)


@router_profession.get('/{profession_id}/', response_model=list(ProfessionSchemas))
def get_professions(profession_id: int, db: Session = Depends(get_db)):
    result = db.query(
        models.Profession
    ).filter(profession_id=profession_id).all()
    if result is None:
        raise HTTPException(
            f'Выбранной {result} профессие нет в списке, выберете другую!'
        )
    return result

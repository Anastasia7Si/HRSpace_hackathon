from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api_v1.core.config import get_db
from api_v1.app import crud
from api_v1.app.schemas import ProfessionModel

router = APIRouter(tags=["Profession"])


@router.get('/{id}/', response_model=ProfessionModel)
async def get_profession_id(id: int, db: Session = Depends(get_db)):
    result = await crud.get_profession_id(id=id, db=db)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {result} not found!",
        )
    return result

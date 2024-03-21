from sqlalchemy.orm import Session

from api_v1.core.db.api_models import Profession
from .schemas import ProfessionModel


async def create_profession(profession: ProfessionModel, db: Session):
    result = Profession(**profession.dict())
    db.add(result)
    db.commit()
    db.refresh(result)
    return await ProfessionModel.from_orm(profession)


async def get_profession_id(db: Session, id: int):
    return await db.query(Profession).filter(Profession.id == id).all()

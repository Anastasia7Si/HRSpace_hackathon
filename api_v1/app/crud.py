from sqlalchemy.orm import Session

from api_v1.core.db.api_models import Profession


async def get_profession_id(db: Session, id: int):
    return await db.query(Profession).filter(Profession.id == id).all()

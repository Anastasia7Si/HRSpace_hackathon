from sqlalchemy.orm import Session
from typing import Type


def get_items_for_models(id: int, db: Session, model: Type):
    return db.query(model).filter(model.id == id).all()

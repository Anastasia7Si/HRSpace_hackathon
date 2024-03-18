from pydantic import BaseModel


class ProfessionModel(BaseModel):

    id: int
    title: str

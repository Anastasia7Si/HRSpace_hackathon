from pydantic import BaseModel


class EmploeyExperienceSchemas(BaseModel):

    id: int
    experience: str


class EducationSchemas(BaseModel):

    id: int
    education: str


class WorkerSchemas(BaseModel):

    description_emploey: str


class WorkerSkills(BaseModel):

    id: int
    skills: str


class WorkerRequirementsSchemas(BaseModel):

    employee_requirements: str

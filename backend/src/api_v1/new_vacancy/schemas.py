from pydantic import BaseModel


class EmployeeExperienceSchemas(BaseModel):

    id: int
    experience: str


class EducationSchemas(BaseModel):

    id: int
    education: str


class WorkerSkills(BaseModel):

    id: int
    skills: str


class AboutEmployerSchemas(BaseModel):

    name_organization: str
    title: str


class DescriptionSchemas(BaseModel):

    description_emploey: str
    employee_requirements: str

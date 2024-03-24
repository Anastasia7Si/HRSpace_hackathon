from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)
from sqlalchemy.orm import relationship

from .database import Base


class CityOrm(Base):
    """Модель для списка Мест работы."""

    __tablename__ = 'City'
    id: int = Column(Integer, primary_key=True, nullable=False)
    region: str = Column(String, nullable=False)
    city: str = Column(String, nullable=False)

    applications = relationship('ApplicationOrm', back_populates='city')
    metro = relationship('MetroOrm', back_populates='city')


class Timezone(Base):
    """Модель часовых поясов."""

    __tablename__ = 'Timezone'
    id: int = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String, nullable=False)


class MetroOrm(Base):
    """Модель для списка Метро."""

    __tablename__ = 'Metro'
    id: int = Column(Integer, primary_key=True, nullable=False)
    metro: str = Column(String, nullable=False)
    city_id: int = Column(Integer, ForeignKey('City.id'))

    city = relationship('CityOrm', back_populates='metro')
    applications = relationship('ApplicationOrm', back_populates='metro')


class Profession(Base):
    """Модель для списка Профессий."""

    __tablename__ = "professions"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    applications = relationship("Applications", backref="professions")


class PaymentSchema(Base):
    """Модель для списка Схем оплат."""

    __tablename__ = "payment_schemas"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)


class RecruiterResponsibilities(Base):
    """Модель Обязанностей рекрутера."""

    __tablename__ = "recruiter_responsibilities"
    id = Column(Integer, primary_key=True, nullable=False)
    responsibility = Column(String, nullable=False)


class ApplicationOrm(Base):
    """Модель Заявки(вакансии)."""

    __tablename__ = "Applications"

    id = Column(Integer, primary_key=True, nullable=False)
    number_of_employees = Column(Integer, nullable=True)
    payment_amount = Column(Integer, nullable=False)
    title = Column(String, nullable=True)
    description_emploey = Column(String, nullable=True)
    employee_requirements = Column(String, nullable=True)
    number_of_recruiters = Column(Integer, nullable=True)
    id_experience = Column(
        Integer, ForeignKey("experiences.id"), nullable=True
        )
    id_education = Column(
        Integer, ForeignKey("educations.id"), nullable=True
        )
    id_skills = Column(
        Integer, ForeignKey("skills.id"), nullable=True
        )
    id_profession = Column(
        Integer, ForeignKey("professions.id"), nullable=True
        )
    additional_conditions = Column(String, nullable=True)
    bonuses = Column(String, nullable=True)
    salary = Column(Integer, nullable=True)
    id_experience = Column(
        Integer, ForeignKey("experiences.id"), nullable=True
        )
    id_education = Column(
        Integer, ForeignKey("educations.id"), nullable=True
        )
    id_skills = Column(
        Integer, ForeignKey("skills.id"), nullable=True
        )
    id_profession = Column(
        Integer, ForeignKey("professions.id"), nullable=True
        )
    city_id: int = Column(Integer, ForeignKey('City.id'))
    metro_id: int = Column(Integer, ForeignKey('Metro.id'))
    relocation: bool = Column(Boolean, nullable=False, default=False)
    remote_work: bool = Column(Boolean, nullable=False, default=False)
    timezone_from_id: int = Column(
        Integer, ForeignKey('Timezone.id'), nullable=True
        )
    timezone_to_id: int = Column(
        Integer, ForeignKey('Timezone.id'), nullable=True
        )
    city = relationship('CityOrm', back_populates='applications')
    metro = relationship('MetroOrm', back_populates='applications')
    timezone_from = relationship(
        'Timezone', foreign_keys='[ApplicationOrm.timezone_from_id]'
        )
    timezone_to = relationship(
        'Timezone', foreign_keys='[ApplicationOrm.timezone_to_id]'
        )


class WorkerExperience(Base):
    """Модель опыта работы"""

    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, nullable=False)
    experience = Column(String, nullable=False)
    applications = relationship("Application", backref="experience")


class WorkerEducation(Base):
    """Модель образования"""

    __tablename__ = "educations"

    id = Column(Integer, primary_key=True, nullable=False)
    education = Column(String, nullable=False)
    applications = relationship("Application", backref="education")


class WorkerSlills(Base):
    """Модель ключевые навыки"""

    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, nullable=False)
    skills = Column(String, nullable=False)
    applications = relationship("Application", backref="skills")


class AboutEmployer(Base):
    """Модель для работодателя"""

    __tablename__ = "aboute_employers"

    id = Column(Integer, primary_key=True, nullable=False)
    name_organization = Column(String, nullable=False)
    title = Column(String, nullable=False)

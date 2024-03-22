from .database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, ForeignKey
from sqlalchemy.orm import relationship


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


class ApplicationOrm(Base):
    """Модель Заявки(вакансии)."""

    __tablename__ = 'Application'
    id: int = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String, nullable=False)

    # number_of_recruiters = Column(Integer, nullable=True)
    # recruiter_responsibilities = Column(Integer, primary_key=True, nullable=False) # object of RecruiterResponsibilities model
    # experience = Column(String, nullable=True) # поле для опыта работы
    # education = Column(String, nullable=True) # поле образование
    # description_emploey = Column(String, nullable=True) # поле для описания обязанностей сотрудника
    # employee_requirements = Column(String, nullable=True) # поля для описания требований к сотруднику
    # skills = Column(String, nullable=True) # поле ключевые навыки

    # profession = Column(String, primary_key=True, nullable=False) # foreign key, object of profession model
    city_id: int = Column(Integer, ForeignKey('City.id'))
    metro_id: int = Column(Integer,ForeignKey('Metro.id'))
    relocation: bool = Column(Boolean, nullable=False, default=False)
    remote_work: bool = Column(Boolean, nullable=False, default=False)
    timezone_from_id: int = Column(Integer, ForeignKey('Timezone.id'), nullable=True)
    timezone_to_id: int = Column(Integer, ForeignKey('Timezone.id'), nullable=True)

    city = relationship('CityOrm', back_populates='applications')
    metro = relationship('MetroOrm', back_populates='applications')
    timezone_from = relationship('Timezone', foreign_keys='[ApplicationOrm.timezone_from_id]')
    timezone_to = relationship('Timezone', foreign_keys='[ApplicationOrm.timezone_to_id]')

    # salary = Column(Integer, nullable=True)
    # work_schedule = рабочий график, непонятен тип поля, но тоже объект какой-то модели
    # type_of_employment = Column(String, nullable=True) # object of employment model (full-time, part-time)
    # responsibilities = Column(String, nullable=True)
    # requirements = Column(String, nullable=True)
    # stop_list = Column(String, nullable=True)

    # created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    # is_published = Column(Boolean, server_default='FALSE') # может переделать в "статус", типа "на модерации", "размещено", "выполнена"
    # is_moderated = Column(Boolean, server_default='FALSE') # прошла ли заявка модерацию, только после модерации можно оплатить заявку
    # is_paid = Column(Boolean, server_default='FALSE') # оплачена ли заявка, после оплаты попадает в список заявок для Рекрутеров
    # author = User


class WorkerExperience(Base):
    """Модель опыта работы"""

    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, nullable=False)
    experience = Column(String, nullable=False)


class WorkerEducation(Base):
    """Модель образования"""

    __tablename__ = "educations"

    id = Column(Integer, primary_key=True, nullable=False)
    education = Column(String, nullable=False)


class WorkerSlills(Base):
    """Модель ключевые навыки"""

    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, nullable=False)
    skills = Column(String, nullable=False)

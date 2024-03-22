from .database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, ForeignKey
from sqlalchemy.orm import relationship


# class ApplicationsCitiesOrm(Base):
#     """Модель для связи ManyToMany."""
#
#     __tablename__ = "applications_cities"
#     application_id = Column(Integer, ForeignKey('Application.id'), primary_key=True)
#     city_id = Column(Integer, ForeignKey('City.id'), primary_key=True)


# class ApplicationMetro(Base):
#     __tablename__ = "ApplicationMetro"
#     id = Column(Integer, primary_key=True, nullable=False)
#     application_id = Column(Integer, ForeignKey('Application.id'), on_delete="CASCADE")
#     metro_id = Column(Integer, ForeignKey('Metro.id'), on_delete="CASCADE")


class CityOrm(Base):
    """Модель для списка Мест работы."""

    __tablename__ = 'City'
    id: int = Column(Integer, primary_key=True, nullable=False)
    region: str = Column(String, nullable=False)
    city: str = Column(String, nullable=False)
    applications = relationship('ApplicationOrm', back_populates='city')


class Timezone(Base):
    __tablename__ = 'Timezone'
    id: int = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String, nullable=False)

# class MetroOrm(Base):
#     """Модель для списка Мест работы."""
#
#     __tablename__ = "Metro"
#     id = Column(Integer, primary_key=True, nullable=False)
#     city = Column(String, nullable=False)
#     metro = Column(String, nullable=False)


class Profession(Base):
    """Модель для списка Профессий."""

    __tablename__ = "professions"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)


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

    __tablename__ = 'Application'
    id: int = Column(Integer, primary_key=True, nullable=False)
    # number_of_employees = Column(Integer, nullable=True)
    # payment_schema = Column(Integer, primary_key=True, nullable=False) # object of PaymentSchema
    # payment_amount = Column(Integer, nullable=False)
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
    relocation: bool = Column(Boolean, nullable=False, default=False)
    remote_work: bool = Column(Boolean, nullable=False, default=False)
    timezone_from_id: int = Column(Integer, ForeignKey('Timezone.id'), nullable=True)
    timezone_to_id: int = Column(Integer, ForeignKey('Timezone.id'), nullable=True)
    timezone_from = relationship('Timezone', foreign_keys='[ApplicationOrm.timezone_from_id]')
    timezone_to = relationship('Timezone', foreign_keys='[ApplicationOrm.timezone_to_id]')
    city = relationship('CityOrm', back_populates='applications')
    # metro = relationship('MetroOrm', secondary=ApplicationMetro.__table__, backref='Metro')  # many to many, object of city model
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

from .database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


class City(Base):
    """Модель для списка Городов."""

    __tablename__ = "citys"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)


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


class Application(Base):
    """Модель Заявки(вакансии)."""

    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, nullable=False)
    number_of_employees = Column(Integer, nullable=True)
    # payment_schema = Column(Integer, primary_key=True, nullable=False) # object of PaymentSchema
    payment_amount = Column(Integer, nullable=False)
    title = Column(String, nullable=True)
    # date_of_first_resume = жедаемая дата получения первых резюме
    # date_of_first_workday = желаемя дата выхода сотрудника на работу
    number_of_recruiters = Column(Integer, nullable=True)
    # recruiter_responsibilities = Column(Integer, primary_key=True, nullable=False) # object of RecruiterResponsibilities model
    experience = Column(String, nullable=True) # поле для опыта работы
    education = Column(String, nullable=True) # поле образование
    description_emploey = Column(String, nullable=True) # поле для описания обязанностей сотрудника
    employee_requirements = Column(String, nullable=True) # поля для описания требований к сотруднику
    skills = Column(String, nullable=True) # поле ключевые навыки

    # profession = Column(String, primary_key=True, nullable=False) # foreign key, object of profession model
    # city = Column(String, nullable=True) # many to many, object of city model
    salary = Column(Integer, nullable=True)
    # work_schedule = рабочий график, непонятен тип поля, но тоже объект какой-то модели
    type_of_employment = Column(String, nullable=True) # object of employment model (full-time, part-time)
    responsibilities = Column(String, nullable=True)
    requirements = Column(String, nullable=True)
    stop_list = Column(String, nullable=True)

    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    is_published = Column(Boolean, server_default='FALSE') # может переделать в "статус", типа "на модерации", "размещено", "выполнена"
    is_moderated = Column(Boolean, server_default='FALSE') # прошла ли заявка модерацию, только после модерации можно оплатить заявку
    is_paid = Column(Boolean, server_default='FALSE') # оплачена ли заявка, после оплаты попадает в список заявок для Рекрутеров
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

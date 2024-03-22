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

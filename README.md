# HRSpace_hackathon
Репозиторий backend для участия в хакатоне HRSpace

## Авторы

- [Владимир Раскин](https://github.com/v0vanjke)
- [Никита Лоскутов](https://github.com/ragecodemode)
- [Анастасия Пушкарная](https://github.com/Anastasia7Si)

<div id="header" align="center">
  <img src="https://img.shields.io/badge/Python-3.11-F8F8FF?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-0.104.1-F8F8FF?style=for-the-badge&logo=FastAPI&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-555555?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0.23-F8F8FF?style=for-the-badge&logo=SQLAlchemy&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-555555?style=for-the-badge&logo=docker&logoColor=2496ED">
  <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
</div>

## Технологии

**Client:** Python 3.11 , Fastapi 0.104, Uvicorn 0.24, SQLAlchemy 2.0, alembic 1.12, python-dotenv 1


## Реализация:
Этапы:

    Настройка окружения и установка необходимых инструментов
    Написание приложения с использованием FastAPI
    Создание Dockerfile для сборки контейнера
    Сборка и запуск docker-контейнера с приложением

Задачи:

    Инициализация проекта в IDE и создание структуры приложения
    Написание API-маршрутов и бизнес-логики для приложения с использованием FastAPI
    Настройка зависимостей и настройка конфигурации приложения
    Создание Dockerfile для образа вашего приложения
    Сборка Docker-образа и запуск контейнера для вашего приложения

Цели:

    Обеспечить создание качественного бэкенда с помощью FastAPI
    Сделать приложение портативным и легко масштабируемым через использование Docker-контейнеров
    Обеспечить удобство развертывания и управления приложением.

## Запуск проекта

### Для запуска проекта локально (доступ по http://127.0.0.1:8000/)

- Клонировать репозиторий и перейти в него:
```
git clone git@github.com:Anastasia7Si/HRSpace_hackathon.git
cd HRSpace_hackathon
```
- Создать файл .env в корневой директории и прописать в него свои данные.
Пример:
```
POSTGRES_PASSWORD=db_password
POSTGRES_USER=db_user
POSTGRES_DB=db_name
POSTGRES_PORT=db_port
POSTGRES_SERVER=db_host_name
```
- Подготовить сервер PostgreSQL согласно данным в вашем .env-файле.

- Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
- Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
- Создать и применить миграции:
```
alembic revision --autogenerate -m "migration"
alembic upgrade head
```
- Запустить проект:
```
uvicorn src.main:app
```

### Для запуска контейнеров (доступ по http://localhost:80/)
- Создать файл .env в корневой директории и прописать в него свои данные:

- Запустить сборку  проекта:
```
docker compose -f docker-compose.yml up -d
```

## К проекту подключена документация, в которой можно ознакомиться с эндпоинтами и методами, а также с примерами запросов, ответов и кода:
```
http://127.0.0.1:8000/docs/
```

alembic current

alembic revision --autogenerate -m "migration"

alembic upgrade head

exec uvicorn backend.src.main:app --host 0.0.0.0 --port 8000
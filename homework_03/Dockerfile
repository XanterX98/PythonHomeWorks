# - Для запуска приложения соберите образ
#   `docker build . -t fastapi`
# - Поднимите контейнер с пробросом порта 8000
#   `docker run -p 8000:8000 fastapi`

FROM python:3.9.12-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry==1.1.13
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY app.py .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]
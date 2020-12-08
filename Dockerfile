FROM tiangolo/uvicorn-gunicorn:python3.7

RUN pip install --no-cache-dir fastapi

COPY ./app /app
FROM python:3.7-alpine

WORKDIR /app
COPY src/ /app/src/
COPY requirements /app
COPY application.ini /app
COPY main.py /app

RUN python3 -m pip install -r requirements

ENV ENVIRONMENT DEV
CMD ["python", "/app/main.py"]
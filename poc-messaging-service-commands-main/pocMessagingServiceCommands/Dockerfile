FROM python:3.11.5-bookworm

ADD . /app/
WORKDIR /app

ARG KEYCLOAK_PUBLIC_KEY=""
ARG KEYCLOAK_ALG=""
ARG BOOTSTRAP_SERVER=""
ARG TOPIC=""
ARG ENV=""

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && python manage.py migrate

EXPOSE 80

CMD python -m uvicorn pocMessagingServiceCommands.asgi:application --host 0.0.0.0 --port 80
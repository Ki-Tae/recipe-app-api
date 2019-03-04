FROM python:3.7-alpine
MAINTAINER dave khim

ENV PYTHONUNBUFFERED 1
# recommended env variable

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
# for safety issue
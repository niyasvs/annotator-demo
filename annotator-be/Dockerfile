# Dockerfile

# pull the official docker image
FROM python:3.10.5-slim

# set work directory
WORKDIR /annotator-be/app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
FROM python:3.8-slim

COPY requirements-processing.txt requirements.txt

# install gcc
RUN apt-get update
RUN apt-get install gcc -y
RUN apt-get clean -y

ENV PYTHONUNBUFFERED=TRUE

# install python dependencies
RUN pip install -r requirements.txt
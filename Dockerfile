FROM python:buster

COPY requirements.txt /tmp/
RUN pip install -r requirements.txt

RUN mkdir
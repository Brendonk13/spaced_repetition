
FROM python:3.9-slim-buster

WORKDIR /api
# TODO: change this to just pip install -r requirements.txt
RUN pip install -Iv django==4.1
RUN pip install -Iv djangorestframework==3.14.0
COPY src /api

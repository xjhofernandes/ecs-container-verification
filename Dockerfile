FROM python:3.8-slim

RUN pip install requests click

COPY . /my-app

WORKDIR /my-app

ENTRYPOINT [ "bash", "script.sh" ]

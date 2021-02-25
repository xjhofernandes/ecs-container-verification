FROM python:3.8-slim

RUN pip install requests

COPY . /my-app

WORKDIR /my-app

CMD ["python", "main.py"]

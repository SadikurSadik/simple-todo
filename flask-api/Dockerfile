FROM python:latest

WORKDIR /app

COPY . /app

RUN apt-get update && pip install -r requirements.txt

EXPOSE 5000

CMD python ./index.py
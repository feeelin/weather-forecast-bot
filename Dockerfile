FROM python:3.11.9-alpine3.20
LABEL authors="feelin"

ENTRYPOINT ["top", "-b"]

WORKDIR ./bot
COPY . .

RUN pip install -r requirements.txt
RUN python3 main.py

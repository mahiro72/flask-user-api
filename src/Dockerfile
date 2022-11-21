FROM python:alpine

RUN apk --no-cache add build-base
RUN apk --no-cache add postgresql-dev

WORKDIR /root/src

COPY . .

RUN pip install -r requirements.txt
RUN python3 -m pip install psycopg2

CMD ["python", "main.py"]
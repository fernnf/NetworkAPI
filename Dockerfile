FROM python:3.7.4-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add git

RUN mkdir /code
WORKDIR /code
RUN git clone https://github.com/fernnf/NetworkAPI.git
WORKDIR /code/NetworkAPI

RUN pip3 install --requirement requirements.txt
RUN python3 manage.py makemigrations && python3 manage.py migrate
RUN python3 manage.py loaddata db.json

CMD python3 manage.py runserver 0.0.0.0:8000








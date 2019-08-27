FROM ubuntu:latest

RUN apt update
RUN apt install -y python3 python3-pip curl git links

WORKDIR /root

RUN git clone https://github.com/fernnf/NetworkAPI.git

WORKDIR /root/NetworkAPI

RUN pip3 install --requirement requirements.txt

RUN ls

RUN python3 manage.py migrate

RUN python3 manage.py loaddata








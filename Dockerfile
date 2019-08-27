FROM ubuntu:latest

RUN apt update
RUN apt install -y python3 python3-pip curl git

WORKDIR /root

RUN git https://github.com/fernnf/NetworkAPI.git



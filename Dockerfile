FROM ubuntu:latest
LABEL maintainer="grimsleepless@protonmail.com"

EXPOSE 80

WORKDIR /opt/site

RUN apt update && apt dist-upgrade -y \
        && apt install python3 python3-dev

COPY . /opt/site



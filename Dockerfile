FROM ubuntu:latest
LABEL maintainer="grimsleepless@protonmail.com"

EXPOSE 80

WORKDIR /opt/app

RUN apt update && apt dist-upgrade -y \
        && apt install python3 python3-dev

COPY requirements.txt /opt/app/requirements.txt
RUN pip3 install -r /opt/app/requirements.txt

COPY src /opt/app
ENTRYPOINT [ ]

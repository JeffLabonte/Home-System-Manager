FROM python:3
LABEL maintainer="grimsleepless@protonmail.com"

EXPOSE 8080
ENV LANG en_US.utf8
WORKDIR /opt/app

RUN apt update && apt install build-essential -y

COPY Makefile Makefile
COPY requirements/ requirements/

RUN sed -i 's/sudo//g' Makefile && \
    pip install --upgrade pip
RUN make deps_dev

COPY src /opt/app
ENTRYPOINT [ ]

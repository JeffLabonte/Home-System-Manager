FROM python:3
LABEL maintainer="grimsleepless@protonmail.com"

EXPOSE 8080
ENV DB_PORT=5432
WORKDIR /opt/app

RUN apt update && apt install build-essential -y

COPY Makefile Makefile
RUN sed -i 's/sudo//g' Makefile
COPY requirements/ requirements/
RUN make deps_dev

COPY src /opt/app
ENTRYPOINT [ ]

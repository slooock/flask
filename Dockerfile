FROM alpine:3.14

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN apk add g++
RUN apk add python3-dev
COPY requirements.txt tmp
RUN pip3 install -r tmp/requirements.txt
EXPOSE 5000

ENTRYPOINT cd src && python3 run.py
FROM python:3.8-alpine3.12
RUN mkdir /server
WORKDIR /server
COPY ./requirements.txt /
RUN apk update \
    && rm -rf /var/cache/apk/*  \
    && rm -rf /tmp/* \
    && apk add python3 postgresql-libs \
    && apk add --no-cache gcc libffi-dev g++ python3-dev build-base linux-headers postgresql-dev \
    && apk add --no-cache postgresql-contrib pcre-dev bash alpine-sdk jpeg-dev zlib-dev \
    && pip install -U setuptools pip
COPY . /server/
RUN pip install -r /requirements.txt && PATH=/usr/local/bin:$PATH

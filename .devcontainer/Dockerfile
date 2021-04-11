FROM python:3.8-slim-buster as build

RUN apt-get update --yes && \
    apt-get install --no-install-recommends --yes \
        curl=7.* \
        fish=3.* && \
    rm -rf /var/lib/apt/lists/*

SHELL ["/usr/bin/fish", "-c"]

COPY requirements.txt /tmp/pip-tmp/
RUN pip install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp
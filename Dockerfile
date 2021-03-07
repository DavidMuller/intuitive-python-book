FROM python:3.8.8-slim

RUN groupadd --system monty && useradd --no-log-init --system --shell /bin/bash --gid monty monty

USER monty

COPY --chown=monty code/ /code

WORKDIR /code

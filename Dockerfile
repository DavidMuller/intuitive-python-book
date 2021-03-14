FROM python:3.9.2

RUN groupadd --system monty && useradd --create-home --no-log-init --system --shell /bin/bash --gid monty monty

USER monty

# pip adds bin shortcuts like `flake8` to `/home/monty/.local/bin`
ENV PATH="/home/monty/.local/bin:${PATH}"

COPY --chown=monty requirements.txt /requirements.txt
RUN python -m pip install -r requirements.txt --require-hashes
RUN rm -rf $(pip cache dir)

COPY --chown=monty code/ /home/monty/code

WORKDIR /home/monty/code

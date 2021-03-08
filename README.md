# Intuitive Python: Productive Development for Projects

This repository contains the source code and companion Docker image for [Intuitive Python: Productive Development for Projects](https://pragprog.com/titles/dmpython).

## How To Use the Companion Docker Image

The companion Docker image contains an appropriate version of Python and all the book's source code. To use the companion image, do the following:

1. [Install Docker](https://docs.docker.com/get-docker/).
2. Run: `docker run --pull=always --interactive --tty --rm ghcr.io/davidmuller/intuitive-python-book/intuitive-python-book:latest /bin/bash`

After executing step 2, you'll be logged into the Docker container as a user named `monty` in a directory with all the book's source code. Use this space as a sandbox to run all the code examples as you read [the book](https://pragprog.com/titles/dmpython).

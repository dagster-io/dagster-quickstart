FROM mcr.microsoft.com/devcontainers/python:3.11

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y gdal-bin libgdal-dev g++

COPY setup.py .

# Hotfix: https://github.com/astral-sh/uv/issues/1374#issuecomment-1950266614
ENV VIRTUAL_ENV /usr/local/

RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && . $HOME/.cargo/env \
    && uv pip install -e .[dev]

COPY . .

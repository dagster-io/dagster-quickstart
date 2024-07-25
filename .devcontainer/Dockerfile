FROM mcr.microsoft.com/devcontainers/python:3.11

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y gdal-bin libgdal-dev g++

COPY setup.py .


RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && . $HOME/.cargo/env  \
    && uv venv \
    && uv pip install --system -e .[dev]

COPY . .

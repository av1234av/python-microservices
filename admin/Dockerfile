FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN set -ex; \
    pip install -r requirements.txt; \
    addgroup --gid 1000 user; \
    adduser --disabled-password --gecos '' --uid 1000 -gid 1000 user
USER user
COPY . /app

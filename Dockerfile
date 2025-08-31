FROM python:3.11-slim-bullseye

RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

WORKDIR /project_api

COPY . .

# hadolint ignore=DL3013
RUN pip --no-cache-dir install ".[deploy]"

ENTRYPOINT ["gunicorn", "--forwarded-allow-ips=*", "--bind", "0.0.0.0", "ententes:create_app()"]
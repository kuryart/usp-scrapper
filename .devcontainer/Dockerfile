# Base image
FROM python:3.12.0b3-slim-bullseye

# Copy dependencies file
COPY requirements.txt /tmp/pip-tmp/

# Install dependencies
RUN apt-get update \
    && pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
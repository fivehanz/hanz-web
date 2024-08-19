FROM python:3.11-slim-bookworm as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

############################################################

FROM python-base as builder-base

RUN apt-get update \
    && apt-get install --no-install-recommends -y --quiet \
    curl \
    build-essential \
    postgresql-client \
    libpq-dev \
    inotify-tools \
    && rm -rf /var/lib/apt/lists/* && apt-get clean

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

RUN poetry install --no-dev && poetry add granian[reload] && poetry cache clear . --all

############################################################

FROM python-base as development

RUN apt-get update \
    && apt-get install --no-install-recommends -y --quiet \
    postgresql-client-15 \
    && rm -rf /var/lib/apt/lists/* && apt-get clean

WORKDIR $PYSETUP_PATH

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

WORKDIR /app/src

# Copy the source code into the container
# COPY . /app/

ENV PYTHONUNBUFFERED=1
EXPOSE 8000
ENV PYTHONPATH=/app/src:$PYTHONPATH

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

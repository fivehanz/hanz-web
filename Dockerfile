FROM python:3.11-slim-bookworm AS python-base

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
FROM python-base AS builder-base

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

RUN poetry install --no-dev && poetry add granian==1.5.2 && poetry cache clear . --all

############################################################
FROM python-base AS production

RUN apt-get update \
    && apt-get install --no-install-recommends -y --quiet \
    postgresql-client-15 \
    && rm -rf /var/lib/apt/lists/* && apt-get clean

ENV GID=1000
ENV UID=1000

RUN groupadd -g $GID wagtail && \
    useradd -m -u $UID -g $GID wagtail

WORKDIR $PYSETUP_PATH
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

WORKDIR /app/src

# Copy the source code into the container
COPY . /app/src/

ENV PYTHONUNBUFFERED=1
ENV PORT=8000
EXPOSE $PORT

# ENV PYTHONPATH=/app/src:$PYTHONPATH

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && chown wagtail:wagtail /entrypoint.sh

RUN chown wagtail:wagtail -R /app/src
#COPY --chown=wagtail:wagtail . .

USER wagtail

ENTRYPOINT ["/entrypoint.sh"]

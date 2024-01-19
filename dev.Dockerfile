FROM python:3.11-slim-bookworm
RUN useradd wagtail
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

EXPOSE ${PORT}

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    postgresql-client \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/* && apt-get clean

# Use /app folder as a directory where the source code is stored.
WORKDIR /app
RUN chown wagtail:wagtail /app
COPY --chown=wagtail:wagtail . .

# Install server
RUN pip --no-cache-dir install granian

# Install the project requirements.
RUN pip --no-cache-dir install pipenv && python -m pipenv requirements > requirements.txt && pip --no-cache-dir install -r requirements.txt

# Install LLM anyScale endpoints
ENV LLM_USER_PATH=/app/.llm
RUN python -m llm install llm-anyscale-endpoints

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# server start
CMD exec granian \
    --interface wsgi hanz.wsgi:application \
    --host 0.0.0.0 \
    --port $PORT \
    --workers 2 \
    --http auto \
    --threading-mode runtime

FROM python:3.11-slim-bookworm

# Add user that will be used in the container.
RUN useradd wagtail

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    # libpq-dev \
    # libmariadbclient-dev \
    # libjpeg62-turbo-dev \
    # zlib1g-dev \
    # libwebp-dev \
 && rm -rf /var/lib/apt/lists/* && apt-get clean

# Use /app folder as a directory where the source code is stored.
WORKDIR /app
RUN chown wagtail:wagtail /app
COPY --chown=wagtail:wagtail . .

# Install the project requirements.
RUN pip --no-cache-dir install pipenv && python -m pipenv requirements > requirements.txt && pip --no-cache-dir install -r requirements.txt

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# Collect static files.
# RUN make build-tailwindcss &&
RUN python manage.py collectstatic --noinput --clear
RUN python manage.py compress --force
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "hanz.wsgi", "-w", "3"]  

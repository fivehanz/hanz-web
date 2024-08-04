#!/bin/bash
set -euo pipefail

run_migrations() {
    echo "----------------- Applying database migrations -----------------"
    python manage.py makemigrations
    python manage.py migrate
}

if [ "${RUN_MIGRATION:-false}" = true ]; then
    run_migrations
else
    echo "----------------- Skipping database migrations -----------------"
fi

echo "--------------------    Starting server    --------------------"
exec "$@"

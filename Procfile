web: gunicorn hanz.wsgi

release: python manage.py compress --force && python manage.py collectstatic --noinput && python manage.py makemigrations && python manage.py migrate

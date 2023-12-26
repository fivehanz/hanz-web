web: gunicorn hanz.wsgi:application

release: python manage.py collectstatic --noinput --clear && python manage.py compress --force && python manage.py collectstatic --noinput && python manage.py makemigrations && python manage.py migrate

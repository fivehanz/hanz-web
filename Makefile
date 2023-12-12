
dev: dev-django
migrate: migrate-django
	
dev-django:
	python manage.py runserver

migrate-django:
	python manage.py makemigrations && python manage.py migrate

shell:
	python -m pipenv shell

install:
	python -m pipenv install

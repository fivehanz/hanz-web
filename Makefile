MAKEFLAGS += -j2

GIT_TAG = ${shell git tag | tail -1}

build: build-tailwindcss build-statics
deps: bun-install python-install
build-docker: build-docker-image
dev: dev-tailwindcss dev-django
migrate: migrate-django


build-docker-image:
	docker build --tag hanz-web:${GIT_TAG} .

run-docker:
	docker run --rm -p 8000:8000 --env-file .env --name hanz-web-${GIT_TAG}-dev hanz-web:${GIT_TAG}

run-docker-prod:
	docker run --rm -p 8000:8000 --env-file .env --env DJANGO_SETTINGS_MODULE=hanz.settings.production --name hanz-web-${GIT_TAG}-prod hanz-web:${GIT_TAG} 

dev-django: 
	python -m pipenv run python manage.py runserver

migrate-django:
	python manage.py makemigrations && python manage.py migrate

dev-tailwindcss:
	bunx --bun tailwindcss -i ./assets/css/input.css -o ./assets/css/output.css --watch --minify

build-tailwindcss:
	bunx --bun tailwindcss -i ./assets/css/input.css -o ./assets/css/output.css --minify

build-statics: 
	python -m pipenv run python manage.py collectstatic --noinput --clear
	python -m pipenv run python manage.py compress --force
	python -m pipenv run python manage.py collectstatic --noinput

shell:
	python -m pipenv shell

bun-install:
	bun --bun install

python-install:
	python -m pipenv install

rtx:
	# brew install libb2 openssl readline gettext
	env PYTHON_CONFIGURE_OPTS="--enable-optimizations --disable-ipv6" env LDFLAGS="-fuse-ld=lld" ARCHFLAGS="-arch arm64" rtx i

deploy:
	fly deploy

logs:
	fly logs -a hanz-web

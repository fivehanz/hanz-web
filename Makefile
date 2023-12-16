MAKEFLAGS += -j2

GIT_TAG = ${shell git tag | tail -1}

install: bun-install python-install
build: build-tailwindcss
dev: dev-tailwindcss dev-django
migrate: migrate-django


build-docker-image:
	docker build --tag hanz-web:${GIT_TAG} .

run-docker:
	docker run --rm -p 8000:8000 --env-file .env hanz-web:${GIT_TAG}

run-docker-prod:
	docker run --rm -p 8000:8000 --env-file .env --env DJANGO_SETTINGS_MODULE=hanz.settings.production hanz-web:${GIT_TAG}

dev-django:
	python manage.py runserver

migrate-django:
	python manage.py makemigrations && python manage.py migrate

dev-tailwindcss:
	bunx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch

build-tailwindcss:
	bunx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --minify

shell:
	python -m pipenv shell

bun-install:
	bun install

python-install:
	python -m pipenv install

rtx:
	# brew install libb2 openssl readline gettext
	env PYTHON_CONFIGURE_OPTS="--enable-optimizations --disable-ipv6" env LDFLAGS="-fuse-ld=lld" ARCHFLAGS="-arch arm64" rtx i

deploy:
	fly deploy

logs:
	fly logs -a hanz-web

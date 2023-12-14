MAKEFLAGS += -j2

build: build-tailwindcss
dev: dev-tailwindcss dev-django
migrate: migrate-django
	
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

install:
	bun install
	python -m pipenv install

rtx:
	# brew install libb2 openssl readline gettext
	env PYTHON_CONFIGURE_OPTS="--enable-optimizations --disable-ipv6" env LDFLAGS="-fuse-ld=lld" ARCHFLAGS="-arch arm64" rtx i

MAKEFLAGS += -j2

GIT_TAG = ${shell git tag | tail -1}

build: build-tailwindcss build-statics
deps: bun-install python-install
build-docker: build-docker-image
dev: dev-tailwindcss dev-django
migrate: migrate-django
prod: prod-release

# ! do not run as root
prod-release:
	sudo make prod-stop
	sudo make prod-rebuild
	sudo make prod-restart
	make prod-static-release
	sudo make prod-migrate
	sudo nginx -s reload

prod-init:
	# write scripts for init 

prod-static-release:
	python3 -m pipenv run python manage.py collectstatic --noinput --clear
	python3 -m pipenv run python manage.py collectstatic --noinput
	python3 -m pipenv run python manage.py compress --force
prod-start: 
	docker compose --env-file .env --file ./deployment/compose/docker-compose.yml up -d
prod-rebuild: 
	docker compose --env-file .env --file ./deployment/compose/docker-compose.yml up -d --build
prod-restart: 
	docker compose --env-file .env --file ./deployment/compose/docker-compose.yml up -d --force-recreate
prod-stop: 
	docker compose --env-file .env --file ./deployment/compose/docker-compose.yml down
prod-migrate: 
	docker exec -it hanz_prod_app make migrate
prod-nginx-link: 
	ln -s ${shell pwd}/deployment/nginx/vhost.conf /etc/nginx/sites-enabled/hanz-web.conf



build-docker-image:
	docker build --tag hanz-web:${GIT_TAG} -f ./Dockerfile .

run-docker:
	docker run --rm -p 8000:8000 --env-file .env --name hanz-web-${GIT_TAG}-dev hanz-web:${GIT_TAG}

run-docker-prod:
	docker run --rm -p 8000:8000 --env-file .env --env DJANGO_SETTINGS_MODULE=hanz.settings.production --name hanz-web-${GIT_TAG}-prod hanz-web:${GIT_TAG} 

dev-django: 
	python -m pipenv run python manage.py runserver

migrate-django:
	python manage.py makemigrations && python manage.py migrate --no-input

dev-tailwindcss:
	bunx --bun tailwindcss -i ./assets/css/input.css -o ./assets/css/output.css --watch --minify

build-tailwindcss:
	bunx --bun tailwindcss -i ./assets/css/input.css -o ./assets/css/output.css --minify

build-statics: 
	python -m pipenv run python manage.py collectstatic --noinput --clear
	python -m pipenv run python manage.py collectstatic --noinput
	python -m pipenv run python manage.py compress --force

shell:
	python -m pipenv shell

bun-install:
	bun --bun install

python-install:
	python -m pipenv install

rtx:
	# brew install libb2 openssl readline gettext
	env PYTHON_CONFIGURE_OPTS="--enable-optimizations --disable-ipv6" env LDFLAGS="-fuse-ld=lld" ARCHFLAGS="-arch arm64" rtx i

# deploy:
# 	fly deploy
#
# logs:
# 	fly logs -a hanz-web

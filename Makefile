build:
	docker compose -f ./local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

down-v:
	docker compose -f local.yml down -v

show-logs:
	docker compose -f local.yml logs

show-logs-api:
	docker compose -f local.yml logs api

make-migrations:
	docker compose -f local.yml run --rm api python manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm api python manage.py migrate

collectstatic:
	docker compose -f local.yml run --rm api python manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm api python manage.py createsuperuser

volume-inspect:
	docker volume inspect src_local_postgres_data

db:
	docker compose -f local.yml exec postgres psql --username=jabari --dbname=medinprint

flake8:
	docker compose -f local.yml exec api flake8 .

black-check:
	docker compose -f local.yml exec api black --check --exclude=migrations .

black-diff:
	docker compose -f local.yml exec api black --diff --exclude=migrations .

black:
	docker compose -f local.yml exec api black --exclude=migrations .

isort-check:
	docker compose -f local.yml exec api isort . --check --skip .venv --skip migrations

isort-diff:
	docker compose -f local.yml exec api isort . --diff --skip .venv --skip migrations

isort:
	docker compose -f local.yml exec api isort . --skip .venv --skip migrations
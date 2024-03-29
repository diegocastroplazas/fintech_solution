CURRENT_DIRECTORY := $(shell pwd)

TESTSCOPE = fintech_solution


help:
	@echo "Docker Compose Help"
	@echo "-----------------------"
	@echo ""
	@echo "Run tests to ensure current state is good:"
	@echo "    make test"
	@echo ""
	@echo "If tests pass, add fixture data and start up the web:"
	@echo "    make begin"
	@echo ""
	@echo "Really, really start over:"
	@echo "    make clean"
	@echo ""
	@echo "See contents of Makefile for more targets."

begin: migrate fixtures start

start:
	@docker-compose up -d

stop:
	@docker-compose stop

status:
	@docker-compose ps

restart: stop start

clean: stop
	@docker-compose rm --force
	@find . -name \*.pyc -delete

build:
	@docker-compose build web

test:
	@docker-compose run --rm web python ./manage.py test ${TESTSCOPE} ${TESTFLAGS}

testwarn:
	@docker-compose run --rm web python -Wall manage.py test ${TESTSCOPE} ${TESTFLAGS}

migrate:
	@docker-compose run --rm web python ./manage.py migrate

fixtures:
	@docker-compose run --rm web python ./manage.py runscript load_all_fixtures

cli:
	@docker-compose run --rm web bash

tail:
	@docker-compose logs -f

superuser:
	@docker-compose run --rm web python ./manage.py createsuperuser

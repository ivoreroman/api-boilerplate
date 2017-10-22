run:
	gunicorn --reload api.app:api

install: install-deps install-githooks

install-deps:
	pip install --upgrade pip
	pip install -r requirements/dev.txt

install-githooks:
	cp git-hooks/pre-commit .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit

test-all:
	tox

test:
	tox -e py35

lint:
	tox -e linters

clean:
	rm -rf .tox

.PHONY: run install install-deps install-githooks test-all test lint clean

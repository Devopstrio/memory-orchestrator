.PHONY: install install-dev format lint test run docker-up docker-down

install:
	pip install .

install-dev:
	pip install -e .[dev]
	pre-commit install

format:
	ruff format .
	ruff check --fix .

lint:
	ruff check .
	mypy src/ tests/ --explicit-package-bases
	bandit -r src/ -c pyproject.toml

test:
	pytest tests/ -v --cov=src

run:
	uvicorn memory_orchestrator.main:app --host 0.0.0.0 --port 8080 --reload

docker-up:
	docker-compose -f infrastructure/docker/docker-compose.yml up -d --build

docker-down:
	docker-compose -f infrastructure/docker/docker-compose.yml down

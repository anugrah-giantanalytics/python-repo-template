.PHONY: install format lint test clean docker-build docker-run

# Variables
PYTHON := python3
VENV := .venv
UV := uv

# Docker variables
IMAGE_NAME := python-microservice
IMAGE_TAG := latest

install:
	$(UV) venv
	$(UV) pip install -e ".[dev]"
	$(UV) pip install pre-commit
	pre-commit install

format:
	black app tests
	isort app tests

lint:
	flake8 app tests
	mypy app tests
	black --check app tests
	isort --check-only app tests

test:
	pytest

clean:
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf **/__pycache__
	rm -rf **/*.pyc
	rm -rf **/*.pyo
	rm -rf **/*.pyd
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

docker-build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

docker-run:
	docker run -p 8000:8000 --env-file .env $(IMAGE_NAME):$(IMAGE_TAG)

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 
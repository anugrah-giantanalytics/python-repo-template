.PHONY: install format lint test clean docker-build docker-run activate

# Variables
PYTHON := python3
VENV := .venv
VENV_PYTHON := $(VENV)/bin/python
VENV_PIP := $(VENV)/bin/pip

# Docker variables
IMAGE_NAME := python-microservice
IMAGE_TAG := latest

install:
	$(PYTHON) -m venv $(VENV)
	$(VENV_PIP) install -e ".[dev]"
	$(VENV_PIP) install pre-commit
	$(VENV)/bin/pre-commit install

activate:
	@echo "To activate the virtual environment, run:"
	@echo "source $(VENV)/bin/activate"

format:
	$(VENV_PYTHON) -m black app tests
	$(VENV_PYTHON) -m isort app tests

lint:
	$(VENV_PYTHON) -m flake8 app tests
	$(VENV_PYTHON) -m mypy app tests
	$(VENV_PYTHON) -m black --check app tests
	$(VENV_PYTHON) -m isort --check-only app tests

test:
	$(VENV_PYTHON) -m pytest

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
	$(VENV_PYTHON) -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

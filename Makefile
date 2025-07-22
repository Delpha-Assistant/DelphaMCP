# Makefile for Delpha MCP Python Package

.PHONY: install run publish clean format lint test venv build

VENV_PYTHON := $(shell [ -x .venv/bin/python ] && echo .venv/bin/python || echo python)
RUFF := $(shell [ -x .venv/bin/ruff ] && echo .venv/bin/ruff || echo ruff)

# Create virtual environment if it doesn't exist
venv:
	@if [ ! -d .venv ]; then \
		echo "💡 Creating virtual environment..."; \
		uv venv; \
	else \
		echo "✅ Virtual environment already exists."; \
	fi

# Install dependencies using uv (ensures venv exists)
install: venv
	uv pip install -e .[dev]

# Run the server using the Python from .venv if available
run:
	$(VENV_PYTHON) -m delpha_mcp

# Publish to PyPI using uv
publish: build
	uv publish

# Remove build artifacts
clean:
	rm -rf dist build *.egg-info __pycache__ delpha_mcp/__pycache__

# Format code with ruff (prefer venv)
format:
	$(RUFF) format delpha_mcp

# Lint code with ruff (prefer venv)
lint:
	$(RUFF) check delpha_mcp

# Run tests using pytest from the venv if available
TEST := $(shell [ -x .venv/bin/pytest ] && echo .venv/bin/pytest || echo pytest)

test: install
	PYTHONPATH=. $(TEST) tests 

build:
	$(VENV_PYTHON) -m build 
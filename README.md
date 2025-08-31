[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12%20%7C%203.13-blue?logo=python&logoColor=white)

# Flask Boilerplate

## included features:
- SQL Alchemy
- JWT Authentification
- Marshmallow Schema
- Testing (w/ pytest)
- OpenAPI documentation
- Linter (ruff & mypy)
- Basic login strategy

## configurations template:
- pyproject
- docker
- ruff
- mypy


# Setup App

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
cp example.env .env
# Edit the .env file to update environment variables as needed

# Run App
flask --app project_api run
```


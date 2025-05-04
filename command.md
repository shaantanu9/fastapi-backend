### Run Project in UV

```bash
uv run fastapi dev
```

### Run Project in Docker

```bash
docker-compose up
```

### Run Ruff For Linting

```bash
uv run ruff check .
```

### Auto-Fix Ruff

```bash
uv run ruff check --fix .
```

### Run the Ruff Formatters

```bash
uv run ruff format .
```



### Run Isort For Sorting Imports

```bash
uv run isort .
```
### Auto-Fix Isort

```bash
uv run isort --profile black .
```



### Run Black For Formatting

```bash
uv run black .
```

### Run Tests

```bash
uv run pytest
```

### Run Tests with Coverage

```bash
uv run pytest --cov=app
```


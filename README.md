Run the APP
```bash
cd backend-fastapi
uvicorn main:app --host

```


<!-- Other Run Method -->
```bash
docker-compose up
```
```bash

docker run -d -p 8000:8000 --name fastapi-backend fastapi-backend
```

# With UV its simple 
```
 uv run fastapi dev
```bash
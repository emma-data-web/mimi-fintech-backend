# Mimi Fintech Backend

A fintech backend API built with FastAPI, following modern Python development practices using **Poetry** for dependency management and **Alembic** for database migrations.



 FastAPI
Poetry
 SQLAlchemy (Async)
 Alembic
 SQLite (Development)
 PostgreSQL (Production)
 Redis
 Pydantic Settings
 JWT Authentication
 Passlib / Bcrypt



Project Structure

```text
app/
├── core/
├── db/
├── models/
├── routers/
├── schemas/
├── services/
├── main.py

alembic/
```

---

## Getting Started

### Clone the repository

```bash
git clone <your-repository-url>
cd mimi-fintech-backend
```

### Install dependencies

```bash
poetry install
```

### Activate the virtual environment

```bash
poetry shell
```

If `poetry shell` is unavailable:

```bash
source .venv/bin/activate
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=sqlite+aiosqlite:///./app.db

SECRET_KEY=your_secret_key

JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Database Migration

Run all migrations:

```bash
poetry run alembic upgrade head
```

Create a new migration:

```bash
poetry run alembic revision --autogenerate -m "describe your changes"
```

Apply new migrations:

```bash
poetry run alembic upgrade head
```

---

## Running the Application

bash
poetry run uvicorn app.main:app --reload


The API will be available at:


http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## Development

Install development tools:

```bash
poetry install --with dev
```

Run tests:

```bash
poetry run pytest
```

Lint the project:

```bash
poetry run ruff check .
```

---

## Production

For production deployments:

* PostgreSQL
* Redis
* Environment Variables
* HTTPS
* Reverse Proxy (Nginx)
* Docker (recommended)

---

## License

This project is for learning and educational purposes.

# Django Reading Progress Tracker

A Django-based REST API for tracking reading progress.

## Prerequisites

- Docker
- Docker Compose

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Build and start the containers:
```bash
docker-compose up --build
```

The application will be available at:
- API: http://localhost:8000/api/progress
- Admin Interface: http://localhost:8000/admin

## Environment Variables

The following environment variables are configured in docker-compose.yml:
- POSTGRES_DB: wiki
- POSTGRES_USER: postgres
- POSTGRES_PASSWORD: sss777p?
- POSTGRES_HOST: db
- POSTGRES_PORT: 5432

## API Endpoints

- `POST /api/progress`: Create a new reading progress entry
- `GET /api/progress`: List all reading progress entries

## Database

PostgreSQL database is accessible:
- From host: localhost:5433
- From containers: db:5432

## Development

To create a superuser:
```bash
docker-compose exec web python backend/manage.py createsuperuser
```

To view logs:
```bash
docker-compose logs -f
```

To stop the application:
```bash
docker-compose down
```

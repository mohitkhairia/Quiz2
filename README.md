# Employee Dashboard

## Overview
Employee Dashboard is a Django-based web application that generates synthetic employee data, stores it in PostgreSQL, exposes RESTful APIs via Django REST Framework, and visualizes analytics using Chart.js. It supports JWT authentication, Dockerized deployment, and includes a health-check endpoint.

## Features
- **Data Generation**: Faker-based synthetic data seeding for Departments, Employees, Attendance, and Performance.
- **PostgreSQL Integration**: Persistent storage with relational models and migrations.
- **REST APIs**: Endpoints for Departments, Employees, filtering, pagination, and aggregation (`/api/employees/avg-salary-by-dept/`).
- **API Documentation**: Swagger UI available at `/swagger/`.
- **Visualization**: Chart.js bar chart displaying average salary by department on `/dashboard/`.
- **Authentication**: JWT token issuance endpoints at `/api/token/` and `/api/token/refresh/`.
- **Health Check**: Simple JSON endpoint at `/health/`.
- **Docker Support**: Containerized services with Docker Compose.
- **CSV Export**: (If implemented) management command or API renderer.

## Requirements
- Docker & Docker Compose
- Python 3.9+
- PostgreSQL (via Docker)

## Setup

1. **Clone repository**  
   ```bash
   git clone https://github.com/mohitkhairia/Quiz2.git
   cd Quiz2
   ```

2. **Environment Variables**  
   Create a `.env` in the project root:
   ```dotenv
   SECRET_KEY=your-secret-key
   DEBUG=False
   ALLOWED_HOSTS=localhost,127.0.0.1
   POSTGRES_DB=employee_dashboard
   POSTGRES_USER=mohitkhairia
   POSTGRES_HOST_AUTH_METHOD=trust
   ```

3. **Build & Run with Docker**  
   ```bash
   docker compose up --build -d
   ```

4. **Access the App**  
   - Swagger UI: `http://localhost:8000/swagger/`  
   - API Root: `http://localhost:8000/api/`  
   - Health Check: `http://localhost:8000/health/`  
   - Dashboard: `http://localhost:8000/dashboard/`

## Data Seeding
```bash
docker compose exec web python manage.py seed_data
```

## Running Locally (Without Docker)

1. Install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Configure `.env` as above.
3. Start PostgreSQL locally and create DB:
   ```bash
   createuser -s mohitkhairia
   createdb -O mohitkhairia employee_dashboard
   ```
4. Run migrations & server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Testing
```bash
docker compose exec web python manage.py test
```



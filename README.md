# FastAPI Task Manager

A backend Task Management API built using FastAPI, SQLAlchemy, Docker, and SQLite.

---

## 🚀 Features

- Create tasks
- View all tasks
- Update tasks
- Delete tasks
- RESTful APIs
- Database integration using SQLAlchemy
- Dockerized application

---

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Docker
- Git & GitHub

---

## 📂 Project Structure

```bash
fastapi-task-manager/
│
├── main.py
├── database.py
├── models.py
├── requirements.txt
├── Dockerfile
├── README.md
```

---

## ▶️ Run Locally

### Clone repository

```bash
git clone https://github.com/janhavix/fastapi-task-manager.git
```

### Move into project folder

```bash
cd fastapi-task-manager
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

#### Windows (Git Bash)

```bash
source venv/Scripts/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI server

```bash
python -m uvicorn main:app --reload
```

---

## 🌐 API Documentation

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

---

## 🐳 Run with Docker

### Build Docker image

```bash
docker build -t fastapi-app .
```

### Run Docker container

```bash
docker run -p 8000:8000 fastapi-app
```

---

## 📌 Future Improvements

- Jenkins CI/CD pipeline
- AWS deployment
- Monitoring with Prometheus & Grafana
- Authentication system

---

## 👩‍💻 Author

Janhavi
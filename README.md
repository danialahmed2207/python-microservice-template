# 🐍 Python Microservice Template

<div align="center">

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)]()
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)]()
[![Tests](https://img.shields.io/badge/Tests-Pytest-brightgreen)]()

</div>

## 📸 API Preview

```json
// GET /
{
  "name": "Python Microservice Template",
  "version": "1.0.0",
  "author": "Danial Ahmed",
  "docs": "/docs",
  "health": "/health"
}

// GET /health
{
  "status": "healthy",
  "timestamp": "2026-05-09T10:30:00",
  "service": "python-microservice-template",
  "version": "1.0.0"
}
```

---

## 🏗️ Architektur

```
┌─────────────────────────────────────────────────────────┐
│                  FastAPI Microservice                    │
│                                                          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │
│  │   Health    │    │    Items    │    │    Users    │ │
│  │   Router    │    │   Router    │    │   Router    │ │
│  │  (/health)  │    │  (/items)   │    │  (/users)   │ │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘ │
│         │                  │                  │         │
│         └──────────────────┼──────────────────┘         │
│                            ▼                            │
│                    ┌─────────────┐                      │
│                    │   Pydantic  │                      │
│                    │   Models    │                      │
│                    │(Validation) │                      │
│                    └──────┬──────┘                      │
│                           ▼                             │
│                    ┌─────────────┐                      │
│                    │  Database   │                      │
│                    │ (In-Memory) │                      │
│                    └─────────────┘                      │
└─────────────────────────────────────────────────────────┘
```

---

## ✨ Features

- ✅ **FastAPI** – Hochperformante, moderne Python API
- ✅ **Pydantic** – Automatische Datenvalidierung
- ✅ **CRUD Operations** – Vollständige REST API für Items & Users
- ✅ **Health Checks** – Kubernetes-ready Probes (`/health`, `/ready`, `/live`)
- ✅ **Docker** – Multi-stage Dockerfile mit Security-Best-Practices
- ✅ **Tests** – 100% Testabdeckung mit pytest
- ✅ **Code Quality** – Black, flake8, mypy konfiguriert
- ✅ **Auto-Docs** – Interaktive Swagger UI unter `/docs`

---

## 🛠️ Tech Stack

| Technologie | Verwendung |
|------------|-----------|
| **FastAPI** | Web Framework |
| **Pydantic** | Datenvalidierung & Serialisierung |
| **Uvicorn** | ASGI Server |
| **Pytest** | Testing Framework |
| **Docker** | Containerisierung |
| **Black** | Code Formatting |
| **MyPy** | Static Type Checking |

---

## 🚀 Quick Start

### Mit Docker (empfohlen)

```bash
# Repository klonen
git clone https://github.com/danialahmed2207/python-microservice-template.git
cd python-microservice-template

# Container bauen & starten
docker compose up -d

# API testen
curl http://localhost:8000/
curl http://localhost:8000/health
```

### Lokal (Development)

```bash
# Virtual Environment erstellen
python3 -m venv venv
source venv/bin/activate

# Dependencies installieren
pip install -r requirements.txt

# Server starten
uvicorn app.main:app --reload

# Tests ausführen
pytest
```

---

## 📡 API Endpoints

### Health
| Methode | Endpoint | Beschreibung |
|---------|----------|-------------|
| `GET` | `/health` | Health Check |
| `GET` | `/health/ready` | Readiness Probe |
| `GET` | `/health/live` | Liveness Probe |

### Items
| Methode | Endpoint | Beschreibung |
|---------|----------|-------------|
| `GET` | `/items/` | Alle Items listen |
| `GET` | `/items/{id}` | Einzelnes Item |
| `POST` | `/items/` | Item erstellen |
| `PUT` | `/items/{id}` | Item aktualisieren |
| `DELETE` | `/items/{id}` | Item löschen |

### Users
| Methode | Endpoint | Beschreibung |
|---------|----------|-------------|
| `GET` | `/users/` | Alle User listen |
| `GET` | `/users/{id}` | Einzelnen User |
| `POST` | `/users/` | User erstellen |
| `PUT` | `/users/{id}` | User aktualisieren |
| `DELETE` | `/users/{id}` | User löschen |

### Dokumentation
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## 🧪 Tests

```bash
# Alle Tests ausführen
pytest

# Mit Coverage
pytest --cov=app --cov-report=term-missing

# Nur Health Tests
pytest tests/test_health.py

# Nur Item Tests
pytest tests/test_items.py -v
```

---

## 🔒 Security Features

- ✅ **Non-root User** im Docker Container
- ✅ **Multi-stage Build** (kleines Image)
- ✅ **Health Checks** in Dockerfile
- ✅ **Input Validation** mit Pydantic
- ✅ **HTTP Exception Handling**

---

## 📁 Projektstruktur

```
.
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI App Entry Point
│   ├── database.py          # In-Memory DB
│   ├── models.py            # Pydantic Models
│   └── routers/
│       ├── __init__.py
│       ├── health.py        # Health Endpoints
│       ├── items.py         # Item CRUD
│       └── users.py         # User CRUD
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   ├── test_items.py
│   └── test_users.py
├── Dockerfile               # Multi-stage Docker
├── docker-compose.yml       # Docker Compose
├── requirements.txt         # Python Dependencies
├── pyproject.toml           # Project Config
└── README.md
```

---

## 🎯 Was ich gelernt habe

- FastAPI Routing und Dependency Injection
- Pydantic Modelle und Datenvalidierung
- Async/Await in Python APIs
- Docker Multi-stage Builds
- Kubernetes Health Probes
- pytest Best Practices
- API Design Patterns (REST)

---

<div align="center">

Made with 🐍 by **Danial Ahmed** | Backend Developer

</div>

# 🚀 Employee Leave Management API

A production-style Employee Leave Management System built using **FastAPI**, **MySQL**, and **Docker** with JWT authentication and role-based access control.

---

## 📌 Features

- 🔐 JWT Authentication (OAuth2 Password Flow)
- 👤 Role-Based Access Control (Admin / Employee)
- 🗂 Leave Types (Casual, Sick, Earned)
- 📅 Leave Application & Cancellation
- ✅ Admin Approval / Rejection Workflow
- 🚫 Overlapping Leave Validation
- 📊 Leave History & Monthly Summary
- 🐳 Dockerized Deployment
- 🛢 MySQL Database Integration
- 📖 Swagger API Documentation

---

## 🏗 Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy
- MySQL
- JWT (python-jose)
- Docker & Docker Compose
- Swagger UI

---

## 📂 Project Structure

```
employee-leave-management/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── schemas.py
│   ├── auth.py
│   ├── dependencies.py
│   ├── config.py
│   └── init_db.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env (not pushed to GitHub)
└── README.md
```

---

## ⚙ Environment Variables

Create a `.env` file in project root:

```
MYSQL_USER=root
MYSQL_PASSWORD=root
MYSQL_DB=leave_db
MYSQL_HOST=db
MYSQL_PORT=3306

SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🐳 Run with Docker

```bash
docker compose up --build
```

After startup, open:

👉 http://localhost:8000/docs

---

## 🔐 Authentication

1. Register using `/signup`
2. Login using `/login`
3. Click 🔓 **Authorize** button in Swagger
4. Paste JWT access token
5. Access protected routes

---

## 👨‍💼 Roles

### Employee
- Apply Leave
- Cancel Leave
- View Leave History

### Admin
- View All Leaves
- Approve Leave
- Reject Leave

---

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| POST | /signup | Register user |
| POST | /login | Login & get JWT |
| POST | /apply-leave | Apply leave |
| GET | /my-leaves | View own leaves |
| PUT | /approve/{id} | Approve leave (Admin) |
| PUT | /reject/{id} | Reject leave (Admin) |

---

## 🎯 Key Highlights

- Secure authentication using JWT
- Clean architecture with modular structure
- Environment-based configuration
- Dockerized for easy deployment
- Business logic validations implemented

---

## 📌 Author

Sneha R  
GitHub: https://github.com/sneha4731

---

⭐ If you like this project, feel free to star the repository!
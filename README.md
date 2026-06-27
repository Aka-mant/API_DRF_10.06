# 🚀 Django REST API — Users Service

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![Django](https://img.shields.io/badge/Django6.0-green.svg)
![DRF](https://img.shields.io/badge/DRF-REST%20API-red.svg)
![JWT](https://img.shields.io/badge/Auth-JWT-orange.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

# 📌 О проекте

Backend REST API сервис для управления пользователями на **Django REST Framework** с аутентификацией через **JWT (SimpleJWT)**.

Проект реализует полный CRUD для пользователей, а также документацию API через Swagger и Redoc.

---

# ⚙️ Технологии

- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite (по умолчанию, можно заменить на PostgreSQL)
- Docker / Docker Compose

---

# 🔐 API Endpoints

## 👤 Users

- `GET /users/` — список пользователей  
- `POST /users/` — создать пользователя  
- `GET /users/{id}/` — получить пользователя  
- `PUT /users/{id}/update/` — полное обновление  
- `PATCH /users/{id}/update/` — частичное обновление  
- `DELETE /users/{id}/delete/` — удалить пользователя  

---

## 🔑 JWT Authentication

- `POST /token/` — получить access/refresh токен  
- `POST /token/refresh/` — обновить access токен  

---

# 📖 Документация API

BASE_HTML → http://localhost:8000/ddd/    
Admin → http://localhost:8000/admin/    
Swagger → http://localhost:8000/swagger/    
Redoc → http://localhost:8000/redoc/  

---




# 🛠️ Установка (локально)


1. git clone https://github.com/Aka-mant/API_DRF_10.06.git
2. cd project

3. python -m venv venv
4. venv\Scripts\activate  # Windows

5. pip install -r requirements.txt

6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver


# 🐳 Установка через Docker
📦 1. docker compose build   
🚀 2. docker compose up

или в фоне:

docker compose up -d    
docker compose exec web python manage.py migrate    
docker compose exec web python manage.py createsuperuser

  


# 📂 Структура проекта   

project/    
├── config/  
├── static/     
├── sections/  
├── users/  
├── manage.py   
├── requirements.txt    
├── Dockerfile  
├── docker-compose.yml  
├── entrypoint.sh   
└── README.md   


## 👨‍💻 Автор

Дмитрий Широков (PYTHON511)
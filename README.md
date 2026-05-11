<img width="1254" height="1254" alt="ChatGPT Image 3 мая 2026 г , 20_20_20" src="https://github.com/user-attachments/assets/e26e281a-3835-4cd0-9428-ee5849799cde" />
Finly — Personal Finance REST API (в разработке)

Асинхронный бэкенд для управления личными финансами с чистой архитектурой.

Реализовано на данный момент:
1. Полноценная JWT-аутентификация (access/refresh токены) с использованием bcrypt.
2. Многослойная архитектура: роутеры -> сервисы -> репозитории.
3. Взаимодействие с PostgreSQL через SQLAlchemy 2.0 (асинхронно) и Alembic для миграций.
4. Docker-контейнеризация (приложение + база данных).

Стек: Python 3.12, FastAPI, PostgreSQL, SQLAlchemy, Alembic, Docker, JWT, bcrypt.

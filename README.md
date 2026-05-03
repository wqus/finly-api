Finly — Personal Finance REST API (в разработке)

Асинхронный бэкенд для управления личными финансами с чистой архитектурой.
Реализовано:

Полноценная JWT-аутентификация (access/refresh токены) с использованием bcrypt.

Многослойная архитектура: роутеры -> сервисы -> репозитории.

Взаимодействие с PostgreSQL через SQLAlchemy 2.0 (асинхронно) и Alembic для миграций.

Docker-контейнеризация (приложение + база данных).
Стек: Python 3.12, FastAPI, PostgreSQL, SQLAlchemy, Alembic, Docker, JWT, bcrypt.

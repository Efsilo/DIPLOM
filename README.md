# Дипломный проект: Backend-приложение для автоматизации закупок

## Описание проекта

Сервис автоматизации закупок в розничной сети через REST API.

Пользователи: **покупатели** (оформляют заказы) и **поставщики** (управляют товарами и заказами).

## Основной функционал

- Регистрация, аутентификация (токены), подтверждение email

- Управление корзиной и заказами

- Каталог товаров с фильтрацией по магазинам и категориям

- Импорт товаров из YAML-файлов

- Асинхронная отправка email-уведомлений (Celery + Redis)

- Админка для управления заказами

## Продвинутая часть (Celery + Redis)

- **Celery** настроен для асинхронного выполнения задач

- **Redis** используется как брокер сообщений

- **Задача send\_email\_task** — отправка писем в фоне

- **Импорт товаров** вынесен в фоновую задачу

## Технологии



| Backend | Django 5.0 + DRF |

| База данных | PostgreSQL (в Docker) / SQLite (локально) |

| Асинхронные задачи | Celery 5.3 |

| Брокер | Redis 7 |

| Контейнеризация | Docker, Docker Compose |

| Аутентификация | TokenAuthentication |

## Установка и запуск

### Клонирование


git clone \[URL твоего репозитория]

cd netology\_pd\_diplom

Локальный запуск (Windows / Linux / Mac)

1. Создать и активировать виртуальное окружение

```bash

python -m venv venv

source venv/bin/activate # Linux/Mac

venv\Scripts\activate # Windows

```

2. Установить зависимости

```bash

pip install -r requirements.txt

```

3. Создать миграции и применить их

```bash

python manage.py makemigrations backend

python manage.py migrate

```

4. Запустить сервер

```bash

python manage.py runserver

```

Запуск Celery (асинхронные задачи)

1. Запустить Redis (через Docker)

```bash

docker run -d --name redis -p 6379:6379 redis

```

2. Запустить Celery-воркер

```bash

celery -A netology_pd_diplom worker -l info --pool=solo

```

Запуск через Docker Compose (все сервисы)

```bash
docker-compose up -d --build

```

Приложение будет доступно по адресу: http://localhost:8000

API Endpoints (основные)

```bash
Метод URL Описание

POST /api/user/register Регистрация

POST /api/user/login Вход (токен)

POST /api/user/register/confirm Подтверждение email

GET /api/categories Список категорий

GET /api/products Список товаров

GET/POST/PUT/DELETE /api/basket Работа с корзиной

GET/POST /api/orders Заказы

GET/POST /api/contact Контакты

POST /api/partner/update Импорт товаров (для поставщика)

```

Примеры запросов

```bash
Регистрация пользователя


curl -X POST http://127.0.0.1:8000/api/user/register \\

&#x20; -H "Content-Type: application/json" \\

&#x20; -d '{"first\_name":"Иван","last\_name":"Петров","email":"ivan@test.ru","password":"TestPass123","company":"ООО Ромашка","position":"Директор"}'

Логин (получение токена)


curl -X POST http://127.0.0.1:8000/api/user/login \\

&#x20; -H "Content-Type: application/json" \\

&#x20; -d '{"email":"ivan@test.ru","password":"TestPass123"}'

Получение списка категорий


curl http://127.0.0.1:8000/api/categories

Получение списка товаров


curl http://127.0.0.1:8000/api/products

Добавление товара в корзину (с токеном)


curl -X POST http://127.0.0.1:8000/api/basket \\

&#x20; -H "Authorization: Token ТОКЕН\_ИЗ\_ЛОГИНА" \\

&#x20; -H "Content-Type: application/json" \\

&#x20; -d '{"items":"\[{\\"product\_info\\":1,\\"quantity\\":2}]"}'

Оформление заказа


curl -X POST http://127.0.0.1:8000/api/order \\

&#x20; -H "Authorization: Token ТОКЕН\_ИЗ\_ЛОГИНА" \\

&#x20; -H "Content-Type: application/json" \\

&#x20; -d '{"id":1,"contact":1}'

```

Структура проекта

```bash
netology\_pd\_diplom/

├── backend/                    # Основное приложение (модели, views, API)

│   ├── migrations/             # Миграции БД

│   ├── admin.py

│   ├── apps.py

│   ├── models.py               # Модели данных

│   ├── serializers.py

│   ├── tasks.py                # Celery задачи

│   ├── urls.py                 # API маршруты

│   └── views.py                # Представления

├── netology\_pd\_diplom/       # Настройки Django + Celery

│   ├── settings.py

│   ├── celery.py  	        # Конфигурация Celery

│   └── urls.py

├── manage.py

├── requirements.txt

├── Dockerfile

├── docker-compose.yml

└── README.md

```

Что реализовано

```bash

Базовая часть 

· ✅ Модели: User, Shop, Category, Product, ProductInfo, Parameter, Order, OrderItem, Contact

· ✅ JWT-подобная аутентификация (TokenAuthentication)

· ✅ Регистрация, логин, подтверждение email

· ✅ Фильтрация товаров по магазинам и категориям

· ✅ Пагинация

· ✅ Импорт товаров из YAML

· ✅ Работа с корзиной и заказами

· ✅ Отправка email-уведомлений

Продвинутая часть 

· ✅ Celery настроен для асинхронного выполнения задач

· ✅ Redis как брокер сообщений

· ✅ Задача send_email_task для фоновой отправки писем

· ✅ Docker Compose для развёртывания

```


Автор: Алексеев Федор Вячеславович




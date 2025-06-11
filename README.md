# PaymentProject

---

## Быстрый старт

### 1. Клонирование репозитория

```sh
git clone https://github.com/fasadar2/pymentProject.git
cd paymentProject
```

### 2. Запуск через Docker Compose

```sh
docker-compose up --build
```

- Приложение Django будет доступно на [http://localhost:8000](http://localhost:8000)
- Админка Django: [http://localhost:8000/admin/](http://localhost:8000/admin/)  
  Логин: `admin`  
  Пароль: `admin`

### 3. Остановка

```sh
docker-compose down
```

---

## Структура проекта

- `docker-compose.yml` — описание сервисов (web, db)
- `Dockerfile.django` — сборка Django-приложения
- `Dockerfile.postgres` — сборка контейнера PostgreSQL
- `entrypoint.sh` — скрипт запуска Django, миграций и автосоздания суперпользователя
- `main/` — основное приложение с бизнес-логикой

---

## Переменные окружения (пример)

- `DJANGO_DB_HOST=db`
- `DJANGO_DB_NAME=postgres`
- `DJANGO_DB_USER=postgres`
- `DJANGO_DB_PASSWORD=postgres`
- `DJANGO_SECRET=secret_key`

---

## Документация API

### Swagger

- Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)


---

## Описание моделей

### Wallet (Кошелек)

| Поле    | Тип    | Описание                |
|---------|--------|-------------------------|
| id      | UUID   | Уникальный идентификатор|
| balance | int    | Баланс кошелька         |

---

## Описание эндпоинтов

### Получить баланс кошелька

**GET** `/api/v1/wallets/<uuid:wallet_uuid>`

#### Ответ (200 OK)
```json
{
  "balance": 100
}
```

#### Ошибка (400)
```json
{
  "error": "Wallet not found"
}
```

---

### Операция с кошельком (пополнение/снятие)

**POST** `/api/v1/wallets/<uuid:wallet_uuid>/operation`

#### Тело запроса
```json
{
  "operation_type": "DEPOSIT", // или "WITHDRAW"
  "amount": 50
}
```

- `operation_type` — тип операции: `"DEPOSIT"` (пополнение) или `"WITHDRAW"` (снятие)
- `amount` — сумма операции (целое число)

#### Ответ (200 OK)
```json
{
  "id": "uuid-кошелька",
  "balance": 150
}
```

#### Ошибка: неверный тип операции (400)
```json
{
  "error": "Invalid operations"
}
```

#### Ошибка: кошелек не найден (400)
```json
{
  "error": "Wallet not found"
}
```

---

## Примеры запросов

### Получить баланс

```sh
curl http://localhost:8000/api/v1/wallets/<WALLET_UUID>
```

### Пополнить кошелек

```sh
curl -X POST http://localhost:8000/api/v1/wallets/<WALLET_UUID>/operation \
  -H "Content-Type: application/json" \
  -d '{"operation_type": "DEPOSIT", "amount": 100}'
```

### Снять средства

```sh
curl -X POST http://localhost:8000/api/v1/wallets/<WALLET_UUID>/operation \
  -H "Content-Type: application/json" \
  -d '{"operation_type": "WITHDRAW", "amount": 50}'
```



## Администрирование

- Админка доступна по адресу: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- Логин/пароль: `admin`/`admin`

---

## Swagger

- Swagger: `/swagger/`


---

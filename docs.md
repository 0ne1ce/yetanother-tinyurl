## Основные эндпоинты

- `GET /{tinyurl}/` - перенаправление по короткой ссылке на оригинальный URL.
- `GET /api/v1/{tinyurl}/stats/` - получение статистики переходов по короткой ссылке.
- `POST /api/v1/token/` - получение токена доступа для работы с API.
- `POST /api/v1/token/refresh/` - обновление токена доступа.

## Авторизация

Для использования некоторых эндпоинтов необходимо получить токен доступа, отправив `POST` запрос на `/api/v1/token/` с вашими учетными данными. Обновление токена производится через эндпоинт `/api/v1/token/refresh/`.
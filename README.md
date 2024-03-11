# yetanother-tinyurl

По умолчанию JWT-токены действуют 365 дней
0. Редиректит на оригинальную ссылку после перехода
1. Позволяет сократить ссылку неавторизованному пользователю
2. Позволяет зарегистрироваться
3. Позволяет получить JWT-токен для запросов
4. Позволяет сокращать ссылки и собирать статистику переходов (ip-адрес + время)
5. Позволяет получать статистику по переходам

Roadmap:
(+) API
(+) Docker
(+) Managed PostgreSQL
Документация (написать + добавить эндпоинты)
Group VM Instances
Load Balancer
Domain-Name
SSL

Запуск с одного install.sh


# Сервис коротких ссылок

Сервис коротких ссылок позволяет сокращать длинные URL, предоставляя короткий и удобный альтернативный адрес, который будет перенаправлять пользователя на исходный URL.

## Основные эндпоинты

- `GET /{tinyurl}/` - перенаправление по короткой ссылке на оригинальный URL.
- `GET /api/v1/{tinyurl}/stats/` - получение статистики переходов по короткой ссылке.
- `POST /api/v1/token/` - получение токена доступа для работы с API.
- `POST /api/v1/token/refresh/` - обновление токена доступа.

## Авторизация

Для использования некоторых эндпоинтов необходимо получить токен доступа, отправив `POST` запрос на `/api/v1/token/` с вашими учетными данными. Обновление токена производится через эндпоинт `/api/v1/token/refresh/`.

## Примеры использования

Для получения детальной информации по каждому эндпоинту, а также примеров запросов и ответов, обратитесь к документации API, оформленной в соответствии со стандартом OpenAPI 3.0.




Database Schema:

Table Links
| tinyurl | originalUrl | Author | createDatetime | Redirects |
|---------|-------------|--------|----------------|-----------|

Table Users:
| username | password | 

Table Redirects:

1. User Registration

To register a new user, you would send a POST request to the /api/v1/users/ endpoint with a JSON body containing the username and password. You can use tools like curl, Postman, or any HTTP client library in your preferred programming language to make the request.

Example using curl:

curl -X POST http://localhost:8000/api/v1/users/ -H 'Content-Type: application/json' -d '{"username": "yourusername", "password": "yourpassword"}'

2. Obtaining a JWT Token

After registering, obtain a JWT token by sending a POST request to the token endpoint (you need to add this endpoint to your urls.py if you haven't; it's part of the djangorestframework-simplejwt setup).

Example using curl:

curl -X POST http://localhost:8000/api/token/ -H 'Content-Type: application/json' -d '{"username": "yourusername", "password": "yourpassword"}'

3. Creating a New Link

To create a new shortened link, send a POST request to /api/v1/urls/ with the original URL in the JSON body. If you're authenticated (by including the JWT token in the Authorization header), the link will be associated with your user account.

Example using curl with authentication:

curl -X POST http://localhost:8000/api/v1/urls/ -H 'Content-Type: application/json' -H 'Authorization: Bearer <your_token>' -d '{"originalUrl": "https://example.com"}'


Making an Authorized Request
For an authorized request, the client needs to include an Authorization header with a valid token. This token is typically obtained through your login or token obtain endpoints. The request header should look like this:
curl -X POST http://yourdomain.com/api/v1/urls/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -d '{"originalUrl": "http://example.com"}'



Making an Unauthorized (Non-Authenticated) Request
For an unauthorized or non-authenticated request, simply omit the Authorization header. The system will treat the request as coming from an anonymous user. Here’s how the curl command looks for an unauthorized request:
curl -X POST http://127.0.0.1/api/v1/urls/ \
     -H "Content-Type: application/json" \
     -d '{"originalUrl": "https://ya.ru"}'



4. Accessing the Shortened URL

Access the shortened URL by navigating to /r/<tinyurl_uuid>/ in your web browser, where <tinyurl_uuid> is the UUID of the shortened URL you've created. This will redirect you to the original URL.

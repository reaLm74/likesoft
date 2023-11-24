# Тестовое задание для Python-разработчика Likesoft

Django-приложение для управления книгами в библиотеке.

## Технологии

- Python
- Django
- Django REST
- PostgreSQL
- Celery
- Redis
- Docker

## Как запустить проект:

### Клонирование репозитория:
```sh
git clone https://github.com/realn74/likesoft
```
<details> <summary> Шаблон наполнения .env </summary>

```
SECRET_KEY = 'django-insecure-eick6n9ug90djm0ytune0ytmy6j6-n3c$r+l4%z(6cxzi7r^#'

Подключение к postgresql:

DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='postgres'
DB_HOST='db'
DB_PORT='5432'

Подключение к почтовому серверу для отправки писем при регистрации:

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '435'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'true23@gmail.com'
EMAIL_HOST_PASSWORD = '111111111111111111'
EMAIL_SERVER = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = ['true23@gmail.com']

```
</details>

### Запуск приложения в Docker
Собрать контейнер
```
docker-compose build
```
Запустить docker-compose.yaml
```
docker-compose up
```

Проект запущен и доступен: [http://127.0.0.1:8080/](http://127.0.0.1:8080/)

Пересборка контейнеров
```
docker-compose up -d --build
```
Удалить контейнеры
```
docker-compose down
```

### Пользовательские роли
 - Анонимный пользователь — имеет доступ только к регистрации нового пользователя.
 - Аутентифицированный пользователь — имеет полный доступ.

### Регистрация пользователей
 - Пользователь отправляет POST-запрос с параметрами email, username и password
<details> <summary> Пример запроса </summary>

```http request
   POST http://127.0.0.1:8080/auth/signup/
```

 ```json
{
    "username": "admin",
    "password": "962937",
    "email": "fdh@fos.ter"
}
```
</details>

 
 - Пользователь отправляет POST-запрос с параметрами username и password для получения токена
<details> <summary> Пример запроса </summary>

```http request
   POST http://127.0.0.1:8080/api/api-token-auth/
```

 ```json
{
    "username": "admin",
    "password": "962937"
}
```
Пример ответа

```
{
    "token": "c90db0154b64fd3478e9a9fb1d156999ce9bf320"
}
```

</details>

 - В результате пользователь получает токен и может работать с API проекта, отправляя этот токен с каждым запросом.


<details> <summary> Пример запроса </summary>

```http request
   POST http://127.0.0.1:8080/api/v1/books/
```

 ```json
{
    "title": "Толковый словарь",
    "author": "Ожегов Сергей Иванович",
    "isbn": "9785946666572"
}
```
 </details>

### Админка

  ```
  http://127.0.0.1:8080/admin/
  ```

### Примеры взаимодействия с API


Получение списка книг

  ```
  GET http://127.0.0.1:8080/api/v1/books/
  ```
Получение одной книги

  ```
  GET http://127.0.0.1:8080/api/v1/books/1/
  ```
Добавление книги 

  ```
  POST http://127.0.0.1:8080/api/v1/books/
  ```

 ```json
{
    "title": "Толковый словарь",
    "author": "Ожегов Сергей Иванович",
    "isbn": "9785946666572"
}
```

Изменение книги 

  ```
  PUT http://127.0.0.1:8080/api/v1/books/1/
  ```

 ```json
{
    "title": "Толковый словарь русского языка",
    "author": "Ожегов Сергей Иванович",
    "isbn": "9785170789252"
}
```

Удаление книги

  ```
  DELETE http://127.0.0.1:8080/api/v1/books/1/
  ```

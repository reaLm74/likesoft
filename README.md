# Likesoft

Django-приложение для управления книгами в библиотеке.

<details> 
<summary> Поставленная задача </summary>

**Часть 1: Разработка Django-приложения**

1. Создайте Django-приложение для управления книгами в библиотеке. Каждая книга должна иметь следующие атрибуты:
    - Название
    - Автор
    - Год издания
    - ISBN
2. Реализуйте REST API для управления книгами. API должно предоставлять эндпоинты для:
    - Получения списка всех книг.
    - Получения информации о конкретной книге.
    - Создания новой книги.
    - Обновления информации о книге.
    - Удаления книги.

---

**Часть 2: Работа с базой данных и Celery**

1. Используя Django ORM, создайте модель для хранения информации о пользователях приложения. Модель должна содержать следующие поля:
    - Имя пользователя
    - Электронная почта
    - Дата регистрации (автоматически заполняется при создании пользователя)
2. Используя Celery, реализуйте асинхронную задачу, которая отправляет приветственное электронное письмо пользователю при его регистрации.
3. Обновите API для работы с пользователями, добавив эндпоинт для регистрации нового пользователя. При создании нового пользователя, задача Celery должна запускаться асинхронно для отправки приветственного письма.

---

**Часть 3: Работа с Git и системой контроля версий**

1. Создайте отдельную ветку для разработки новой функциональности в вашем репозитории Git. Назовите ветку, например, `feature/book-management`.
2. Внесите несколько изменений в код, связанных с API для управления книгами. Коммиты должны быть информативными и содержательными.
3. Используя механизм ветвления в Git, создайте отдельную ветку для исправления ошибки в коде вашего приложения. Назовите ветку, например, `bugfix/registration`.
4. Создайте Pull Request (или Merge Request) для слияния веток обратно в основную ветку вашего проекта. Убедитесь, что код проходит проверку тестов и успешно ревью.

---

**Часть 4: Работа с Docker и Redis**

1. Создайте Dockerfile для вашего Django-приложения. Включите все необходимые зависимости.
2. Создайте файл docker-compose.yml, чтобы ваше приложение могло успешно запускаться в контейнере. Включите в файл сервис для вашей базы данных MySQL и для Redis (используемого Celery в качестве брокера).
3. Убедитесь, что приложение в контейнере успешно подключается к MySQL и Redis.

---

**Часть 5: Docker**

1. Разверните ваше Django-приложение в контейнерах Docker.
2. Создайте Dockerfile для вашего Django-приложения. Учтите все необходимые зависимости, включая установку пакетов из файла зависимостей (requirements.txt).
3. Создайте файл docker-compose.yml для контейнеризации вашего приложения. Определите сервисы для Django-приложения, базы данных MySQL и брокера сообщений Celery (Redis).
4. Убедитесь, что ваше приложение в контейнере успешно подключается к базе данных MySQL и Celery внутри их собственных контейнеров.
5. Добавьте команды в docker-compose.yml для инициализации базы данных и применения миграций Django при первом запуске.
6. Предоставьте в README инструкции по сборке и запуску контейнеров. Укажите, как пользователь может взаимодействовать с вашим Django-приложением, находящимся в контейнере.

---

**Примечание:**
Удостоверьтесь, что ваши контейнеры настроены таким образом, чтобы приложение успешно работало в среде Docker.

**Критерии оценки:**

- Корректность и полнота реализации каждого шага задания.
- Чистота и структурированность кода.
- Использование Django-паттернов и лучших практик.
- Наличие комментариев в коде, где это необходимо.
- Успешное выполнение всех шагов задания, включая работу с Git, Docker и Celery.

**Важно:**
Пришлите решение задания в виде ссылки на репозиторий (например, на GitHub). Убедитесь, что ваш репозиторий содержит README файл с инструкциями по запуску приложения и любыми другими необходимыми деталями
</details>

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

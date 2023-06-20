# Продуктовый помощник Foodgram
### Описание
На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
### Технологии
Python 3.9
Django 4.2.1

#### Проект доступен по адресу http://158.160.97.65/
- Тестовые пользователи Логин: user1@mail.com (от 1 до 7)  Пароль: useruser
#### Админ http://158.160.97.65/admin
- Логин: admin  Пароль: adminadmin
#### Документация http://158.160.97.65/api/docs/redoc.html

### Запуск проекта на сервере
1. Установить на сервере nginx, docker и docker-compose.
2. Локально создать контейнеры frontend и backend, запушить проект на GitHub для запуска Actions
3. В контейнере выполнить следующие действия:
- выполнить миграции python manage.py migrate
- создать суперюзера python manage.py createsuperuser
- собрать статику python manage.py collectstatic --no-input
- заполнить базу ингредиентами python manage.py parse_ingredients_csv

### Запуск проекта локально
- Клонируйте репозиторий
```
git@github.com:Irena-bun/foodgram-project-react.git
```
#### Для запуска backend:

- Установите и активируйте виртуальное окружение
```
python -m venv venv && . venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt в папке backend
```
pip install -r requirements.txt
``` 
- Выполните миграции
```
pip install -r requirements.txt
```
- Запустите dev-сервер:
```
python manage.py runserver
```
- Доступ в админ-зону по ссылке http://127.0.0.1:8000/admin
Логин: admin
Пароль: adminadmin

#### Для запуска frontend:
- в Node.js перейдите в папку Frontend и выполнить следующие команды для установки зависимостей и запуска проекта:
```
npm i
npm run start
```
- Сайт доступен по ссылке http://localhost:3000/
Тестовые учетные записи:

user@mail.com
useruser

user2@mail.com
useruser1

user3@mail.com
useruser

### Автор
Бунина Ирена

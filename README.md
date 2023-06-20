# Продуктовый помощник Foodgram
### Описание
На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
### Технологии
Python 3.9
Django 2.2.19
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
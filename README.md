**ФАЙЛЫ README.md, .gitignore УДАЛИТЬ, ЕСЛИ БУДЕТЕ КОПИРОВАТЬ ПРОЕКТ**
# Перед началом
Я удалил в postgres_kr/settings.py SECRET_KEY. Вставьте туда любой пароль
# Что необходимо установить
## PostgreSQL
[PostgreSQL](https://www.postgresql.org/download/)

Создать бд, настроить и выдать все права пользователю admin:
- sudo -u postgres psql
- CREATE DATABASE django_agamirov;
- CREATE USER admin WITH PASSWORD ‘very_strong_password’;
- ALTER ROLE admin SET client_encoding TO 'utf8';
- ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
- ALTER ROLE admin SET timezone TO 'UTC';
- GRANT ALL PRIVILEGES ON DATABASE django_agamirov TO admin;
- GRANT postgres TO admin;
- exit

## Зависимости
Создать в папке c проектом виртуальное окружение и активировать его. Затем выполнить
> pip install -r requirements.txt

## Django 
Сделать миграции:
- cd postgres_kr
- py manage.py migrate

Проверить работоспособность сервера
> py manage.py runserver

# Основная работа
Создать суперпользователя для административной панели, который будет раздавать всем права
> py manage.py createsuperuser

Если возникает ошибка, то мой суперпользователь:
login: admin
password: admin123456

Перейдем в панель администратора на запущенном сайте:
> http://127.0.0.1:8000/admin/

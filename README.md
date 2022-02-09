/ python 3.8 /

Install
---------

Create virtual environment and install python libraries
------------------------------------------------------------------------
/ Установка и активация виртуального окружения /

pip install virtualenv

On Linux:
```
python3 -m venv venv
source venv/bin/activate

```
On Windows:
```
python3 -m venv venv
venv/scripts/activate
```
Перейти в директорию venv.

/ Установка пакетов библиотек /
(файл requirements.txt в текущей директории):
```
pip install -r requirements.txt
```
устанавливаемые пакеты:
```
django
psycopg2
djangorestframework)
pytest
... и сопутствующие
```

Create project
--------------------------------

(здесь имя проекта restproj, имя приложения в составе проекта restapi):
```

django-admin startproject restproj

django-admin startapp restapi
```

(переход в директорию проекта restproj, миграция базы данных):
```

cd  restproj
python manage.py makemigrations
python manage.py migrate
```

(создание пользователя с полномочиями администратора):

python manage.py createsuperuser

(далее надо ввести данные пользователя в диалоге)


Run application:
----------------------
```
python manage.py runserver

(url я оставил по умолчанию http://localhost:8000)
```

Requests:
----------------------
```
/ CLI requests /

(запросы GET из Windows cmd string):

curl -i http://localhost:8000/restapi/usersets/

curl -i http://localhost:8000/restapi/usersets/1/

```
(запросы GET из Windows PowerShell,
использую утилиту curl.exe):
```
curl.exe -i -X POST -H 'Content-Type: application/json' http://127.0.0.1:8000/restapi/usersets/ -d '{""name"":""name 4"", ""email"":""user3@mail.com"", ""password"":""pass4""}'

curl.exe -i -X PATCH -H 'Content-Type: application/json' http://127.0.0.1:8000/restapi/usersets/12/ -d '{""name"":""new name""}'

curl.exe -X DELETE http://127.0.0.1:8000/restapi/usersets/12/
```

Можно делать запросы из браузера на странице
http://127.0.0.1:8000/restapi/usersets/

Run tests:
----------------------

(в директории проекта после установки pytest):

(venv) ...\rest_env\restproj>pytest restapi\test_views.py

(сообщение программы тестирования):

collected 3 items

restapi\test_views.py ...                                                                                        [100%]

======== 3 passed in 2.59s ========


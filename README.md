
# Todo App

A project for Todos.



## Installation

Install project with venv

```bash
  python -m venv venv
  open project directory // cd ToDoApp
  pip Install -r requirements.txt
  python manage.py runserver
```

# use command if you change in database table like name or add new fields    
python manage.py makemigrations
python manage.py migrate

# create superuser 
access admin panel via http://127.0.0.1:8000/admin
username:admin
pwd:admin
python manage.py createsuperuser

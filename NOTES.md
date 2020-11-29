### DEFINITIONS
PYTHON | JAVASCRIPT -> LANGUAGE
NODEJS | DJANGO -> PLATFORM TO BUILD A SERVER AND APP (RUN THE APP BUILD WITH A LANGUAGE)
DJANGO REST FRAMEWORK | EXPRESS | KOA -> FRAMEWORK TO BUILD REST APIS


### PYTHON

### DJANGO
* *config/:* Directory with server configuration, like language, timezone, etc.
* *manage.py:* It's look like a Package.json, contains the scripts to run your app
* *APP_NAME/admin*: It's look like a index/entry point for you app.
* *models:* Representative model (Django default use ORM and create a sqlite when initialize)
* *view:* It's look like a Controller.js


## Setup a Django Server
* First, create your venv to storage all packages from you application:
    `python3 -m venv ./venv`
* After that, active yout terminal to work with python:
    `source venv/bin/activate`
* After this setup, install the DJANGO:
    `pip install django`
* If you wanna validate Django installation,  you can use the command bellow:
    `pip freeze`
* Now, create the Django server config.
    `django-admin startproject config .`
    This command create a folder called Config with server configuration, and a file with name manage.py, this file is something similarly to package.json.
* Start the server.
    `python manage.py runserver`

## Create a App
* To create a new app, run the command bellow:
    `python manage.py startapp app_project_name`

## Create your model, example:
    ```
    from django.db import models

    class students(models.Model):
        name = models.CharField(max_length=50)
        document = models.CharField(max_length=9)

        def __str__(self):
            return self.name
    ```

### Migrate your model to Database
* First, you need create your app reference on Django Config. Inside settings.py file, on INSTALLED_APPS topic, insert your app name:
    ```
    'django.contrib.staticfiles',
    'school'
    ```

* After that, run the command bellow:
    `python manage.py makemigrations`

* The command on top will create a new migration based in your model.py, after that, run this command to sync your model with database:
    `python manage.py migrate`


### Create super user to access admin dashboard
* Create a super user with command bellow: 
    `python manage.py createsuperuser`
* Access your admin dashboard with useradmin access
    `http://127.0.0.1:8000/admin/`



### DJANGO REST
* Install django rest in your application
    `pip install djangorestframework`
* Add the library in your settings.py inside config folder.
    ```
    INSTALLED_APPS = [
        ...
        'rest_framework',
    ]
    ```
* After that, create a serializer.py file inside app, to define de internal data transaction contract.
    ```
    from rest_framework import serializers
    from school.models import Student


    class StudentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Student
            fields = ['id', 'name', 'document']
    ```


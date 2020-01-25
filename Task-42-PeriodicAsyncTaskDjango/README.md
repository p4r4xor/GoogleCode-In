# Sample Periodic Asynchronous task for a Django application 

### Resources
```
https://djangopy.org/how-to/handle-asynchronous-tasks-with-celery-and-django#periodic-tasks
https://stackabuse.com/asynchronous-tasks-in-django-with-redis-and-celery/
https://realpython.com/asynchronous-tasks-with-django-and-celery/
https://realpython.com/django-migrations-a-primer/
```
### Requirements
Check the requirements.txt file and install redis from their official website.

### How its done
* Setup a virtural environment as usual. This is done by `python3 -m venv env` followed by `source env/bin/activate`.
* Install the following python packages.
```
(env) $ pip install Django Celery redis Pillow django-widget-tweaks
(env) $ pip freeze > requirements.txt
```
* Now we create a Django project named `async` by `django-admin startproject async`
* Switch to the project directory and create a Django app. This is done by `python manage.py asyncapp`

(Here async and asyncapp are my project/app names, you're free to use yours)

* Now you'll find `async`, `asyncapp`, `manage.py` in the same location, switch to the `async` directory and create a file named `celery.py`
* My `celery.py` had the following code.
```
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async.settings')

celery_app = Celery('async')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
```
* You'll find a `settings.py` file in the same directory, edit the following in it.
```python
#Add the application name in this list.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'asyncapp'
]

# Go to the end of the code and add this
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
```
* Now go to `__init__.py` file and edit it out as the following.
```python
from .celery import celery_app

__all__ = ('celery_app',)
```
* Things are now set in the project folder, time for the tasks in the application folder
* Create a new file named `tasks.py` and give your tasks required. Mine was to perform addition, and hence addition.
```python
from celery import shared_task

@shared_task(name = "addition")
def add(x, y):
    return x + y
```
* For running tasks periodically, we use a scheduler called celery beat.
* Add the following code to `celery.py` in your project directory.
```python
celery_app.conf.beat_schedule = {
    'periodic addition': {
        'task': 'addition',
        'schedule': 60.0,
        'args': (43, 78) 
    },
}
```
* And you're done XD. Make sure you run `redis-server` in a new terminal before proceeding.
* Run `celery worker -A async --loglevel=info` on your current terminal (this should be done in the directory with manage.py) and activate virtualenv in a new terminal for the current directory.
* Run `celery beat -A async --loglevel=info` in the newer one and wait till the scheduled task wait time.
* You should be finding them like this:
![celery2](https://user-images.githubusercontent.com/59013403/71558563-e35d0400-2a22-11ea-8895-e6207f173a04.png)
* Go back to the previous window and you should be seeing this:
![celery1](https://user-images.githubusercontent.com/59013403/71558581-012a6900-2a23-11ea-9461-7849b1451474.png)




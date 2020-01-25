# Sample Asynchronous task for a Django application

### Resources
```
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

@shared_task
def add(x, y):
    return x + y
```
* Save all the following edited files and return back to the directory containing `manage.py`
* Open two new tabs of your terminal, one should be running `redis-server` and the other should be a copy of your current terminal (venv + the current directory)
* Run `celery worker -A image_parroter --loglevel=info` in the current terminal and switch to the copy terminal.
* Try the following.
```
(env) ┌─[paraxor@parrot]─[~/Downloads/GCI-fedora/AsyncDjango/async/async]
└──╼ $python manage.py shell
Python 3.7.5 (default, Oct 27 2019, 15:43:29) 
[GCC 9.2.1 20191022] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from asyncapp.tasks import add
>>> task = add.delay(32, 49)
>>> print(f"id={task.id}, state={task.state}, status={task.status}")
id=b7494064-54e8-48a3-ab2f-fac4665797f8, state=SUCCESS, status=SUCCESS
>>> task.get()
81
>>> tasktwo = add.delay(321, 342)
>>> tasktwo.get()
663
```
* Switch back to the first terminal and cross verify.
![done2](https://user-images.githubusercontent.com/59013403/71539041-01801280-2904-11ea-87d3-7c6a80524123.png)


from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async.settings')

celery_app = Celery('async')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
celery_app.conf.beat_schedule = {
    #name of the scheduler
    'periodic addition': {
        'task': 'addition',
        'schedule': 60.0,
        'args': (43, 78) 
    },
}
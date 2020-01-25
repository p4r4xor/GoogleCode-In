from celery import shared_task

@shared_task(name = "addition")
def add(x, y):
    return x + y
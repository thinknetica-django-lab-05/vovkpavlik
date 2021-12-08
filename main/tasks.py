from celery import shared_task


@shared_task
def summing(x, y):
    return x + y

@shared_task
def hello():
    return "Hello, Ilya"
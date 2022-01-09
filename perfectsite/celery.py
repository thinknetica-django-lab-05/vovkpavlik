import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'perfectsite.settings')

app = Celery('perfectsite')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    # send messages every week about new ads.
    'new_ads_messages': {
        'task': 'main.tasks.send_new_ads_message_task',
        'schedule': crontab(
            day_of_week='thursday',
            hour=18,
            minute=14
        ),
    },
}

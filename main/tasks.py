from datetime import timedelta

from django.utils import timezone

from celery import shared_task

from main.messages import send_new_ads_message


ENDING_WEEK_DAY = timezone.now()
BEGINNING_WEEK_DAY = ENDING_WEEK_DAY - timedelta(days=7)


@shared_task
def send_new_ads_message_task():
    beginning_week = BEGINNING_WEEK_DAY
    ending_week = ENDING_WEEK_DAY
    send_new_ads_message(beginning_week, ending_week)

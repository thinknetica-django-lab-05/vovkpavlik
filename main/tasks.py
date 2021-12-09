from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils import timezone

from main.models import Ad

ENDING_WEEK_DAY = timezone.now()
BEGINNING_WEEK_DAY = ENDING_WEEK_DAY - timedelta(days=7)


@shared_task
def new_ads_message_task():
    ads = Ad.objects.filter(created_at__range=[BEGINNING_WEEK_DAY, ENDING_WEEK_DAY])
    ads_names = [ad.name for ad in ads]

    user_emails = [user.email for user in User.objects.exclude(subscription=None)]
    company_email = "badwolfproduction@gmail.com"
    subject = "New ads at BadWolfProduction.com"
    message = f"Объявления за прошедшую неделю: {ads_names}"

    send_mail(
        subject,
        message,
        company_email,
        user_emails,
        fail_silently=True,
    )

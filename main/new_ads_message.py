from django.core.mail import send_mail

from django.contrib.auth.models import User
from main.models import Ad


def send_new_ads_message(beginning_week, ending_week):
    ads = Ad.objects.filter(created_at__range=[beginning_week, ending_week])
    ads_names = [ad.name for ad in ads]

    user_emails = [
        user.email for user
        in User.objects.exclude(subscription=None)
    ]
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

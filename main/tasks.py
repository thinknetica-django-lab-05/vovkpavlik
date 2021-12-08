from celery import shared_task
from django.core.mail import send_mail


@shared_task
def new_ads_message_task(user_emails, company_email, subject, message):
    send_mail(
        subject,
        message,
        company_email,
        user_emails,
        fail_silently=True,
    )

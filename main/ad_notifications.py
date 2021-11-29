from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from apscheduler.schedulers.background import BackgroundScheduler

from django.contrib.auth.models import User


def start_emailing(ad):
    sched = BackgroundScheduler(timezone='Europe/Moscow')

    @sched.scheduled_job(
        'cron',
        id='my_job_id',
        args=["sender", "instance", "created"],
        day_of_week="mon",
        hour='20',
        minute=40
    )
    @receiver(post_save, sender=ad)
    def send_new_ad_notification_email(sender, instance, created, **kwargs):
        user_emails = [user.email for user in User.objects.exclude(subscription=None)]
        company_email = "badwolfproduction.com"
        if created:
            title = instance.name
            subject = "ALARM!"
            message = f"Кто-то продает {title}. Спеши посмотреть!"
            send_mail(
                subject,
                message,
                company_email,
                user_emails,
                fail_silently=False,
            )

    sched.start()

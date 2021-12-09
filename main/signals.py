# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from celery import shared_task
#
# from django.contrib.auth.models import User
#
# from main.tasks import new_ads_message_task
#
#
# @shared_task
# def sending_mail(ad):
#     @receiver(post_save, sender=ad)
#     def send_new_ad_notification_email(sender, instance, created, **kwargs):
#         user_emails = [user.email for user in User.objects.exclude(subscription=None)]
#         company_email = "badwolfproduction.com"
#         if created:
#             name = instance.name
#             subject = "Новое объявление"
#             message = f"Кто-то продает {name}. Спеши посмотреть!"
#
#             new_ads_message_task.delay(user_emails, company_email, subject, message)

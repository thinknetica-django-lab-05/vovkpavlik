from django.core.mail import send_mail
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler(timezone='Europe/Moscow')


@scheduler.scheduled_job('cron', id='new_ads_message', day_of_week="mon", hour=10, minute=0)
def send_new_ads_message():
    send_mail(
        "ALARM!",
        "У нас обновление товара!. Спеши посмотреть!",
        "badwolfproduction.com",
        ["vovk.pavlik@bk.ru"],
        fail_silently=True,
    )


scheduler.start()

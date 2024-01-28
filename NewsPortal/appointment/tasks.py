from django.core.mail import send_mail
from django.conf import global_settings


def my_test_job():
    send_mail(
        'Job mail',
        'hello from my job!',
        from_email=global_settings.DEFAULT_FROM_EMAIL,
        recipient_list=global_settings.MANAGERS,
    )


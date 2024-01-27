import django.dispatch
from django.dispatch import receiver, Signal
from django.db.models.signals import post_save, post_delete
from django.core.mail import mail_managers
from .models import Appointment


@receiver(post_save, sender=Appointment)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:          # проверяет, создана модель или нет
        f'{instance.client_name} {instance.date.strftime("%Y-%M-%d")}'
    else:
        f'Appoinment change for {instance.client_name} {instance.date.strftime("%Y-%M-%d")}'
    mail_managers(
        subject=f'{instance.client_name} {instance.date.strftime("%Y-%M-%d")}',
        message=instance.message,
    )
    print(f'{instance.client_name} {instance.date.strftime("%Y-%M-%d")} {instance.message}')


@receiver(post_delete, sender=Appointment)
def notify_managers_appointment_canceled(sender, instance, **kwargs):
    subject = f'{instance.client_name} has canceled his appointment!'
    mail_managers(
        subject=subject,
        message=f'Canceled appointment for {instance.date.strftime("%d %m %Y")}',
    )
    print(subject)


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import mail_managers
from .models import Appointment


@receiver(post_save, sender=Appointment)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:          # проверяет, создана модель или нет
        subject = f'{instance.client_name} {instance.date.strftime("%Y-%M-%d")}'
    else:
        subject = f'Appoinment change for {instance.client_name} {instance.date.strftime("%Y-%M-%d")}'
    mail_managers(
        subject=f'{instance.client_name} {instance.date.strftime("%Y-%M-%d")}',
        message=instance.message,
    )
    print(f'{instance.client_name} {instance.date.strftime("%Y-%M-%d")} {instance.message}')


#
# @receiver(pre_save, sender=Appointment)
# def update_profile(sender, instance, **kwargs):
#     instance.client_name = 'John'
#     instance.message = 'Проверка'
#     instance.save()
#     print(f'Create instance {instance.client_name} {instance.message}')
#     return instance
#
#
# @receiver(post_save, sender=Appointment)
# def update_profile(sender, created, instance, **kwargs):
#     if created:
#         instance.client_name = 'John'
#         instance.message = 'Проверка'
#         instance.save()
#         print(f'Update {instance.client_name} {instance.message}')
#     return instance

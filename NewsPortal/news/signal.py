from datetime import date

from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models.signals import m2m_changed, pre_save

from NewsPortal.work.settings import DEFAULT_FROM_EMAIL
from .models import PostCategory, Post

LOCAL_URL = 'http://localhost:8004'


def send_notify(post, subscribers):
    html_content = render_to_string(
        'account/email/post_email.html',
        {
            'text': post.preview(),
            'link': f'{LOCAL_URL}/news/{post.pk}'
        }
    )
    msg = EmailMultiAlternatives(
        subject=post.title,
        from_email=DEFAULT_FROM_EMAIL,
        to=subscribers
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return redirect('/')


@receiver(m2m_changed, sender=PostCategory)
def notify_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.get_categories()
        subscribers_emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]
            # for subscriber in subscribers:
            #     subscribers_emails += [subscriber.email]

        send_notify(instance, subscribers_emails)


# @receiver(pre_save, sender=Post)
# def notify_limit3_post(sender, instance, **kwargs):
#     today = date.today()   # текущий день
#     post_limit = Post.objects.filter(author=instance.author, time_in__date=today).count()  # число возможных авторов
#     if post_limit >= 3:
#         raise ValidationError('Нельзя публиковать больше 3-х постов в сутки')

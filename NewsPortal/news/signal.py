from django.dispatch import receiver
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models.signals import m2m_changed
from django.conf import settings
from .models import PostCategory


#  отправка сообщений пользователю об создании нового поста с подписанной категорией
def send_notify(post, subscribers):
    html_content = render_to_string(
        'account/email/post_email.html',
        {
            'text': post.preview(),
            'link': f'{settings.SITE_URL}/news/{post.pk}'
        }
    )
    msg = EmailMultiAlternatives(
        subject=post.title,
        from_email=settings.DEFAULT_FROM_EMAIL,
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
            subscribers_emails += [s.email for s in subscribers]  # можно просто s (без email)
            # for subscriber in subscribers:
            #     subscribers_emails += [subscriber.email]

        send_notify(instance, subscribers_emails)


# ---------------------------------------------------------------------------
'''
send_notify(preview, pk, title, subscribers):
    for subscfriber in subscfriber:

    html_content = render_to_string(
        'account/email/post_email2.html',
        {
            'username': subscfriber.username 
            'text': post.preview(),
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )
        msg = EmailMultiAlternatives(
        subject=title,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[subscriber.email],
    )

subscribers_emails += [s.email for s in subscribers]  
можно просто s (без email) и тогда получить имя пользователя
'''


# @receiver(pre_save, sender=Post)
# def notify_limit3_post(sender, instance, **kwargs):
#     today = date.today()   # текущий день
#     post_limit = Post.objects.filter(author=instance.author, time_in__date=today).count()
#     if post_limit >= 3:
#         raise ValidationError('Нельзя публиковать больше 3-х постов в сутки')

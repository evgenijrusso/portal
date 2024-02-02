import datetime
import time
from celery import shared_task
from django.utils import timezone
# from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .models import Post, Category


@shared_task
def hello():
    time.sleep(10)
    print('Hello, John')


# ----------------------------------  task 2 --------------------------------
@shared_task
def send_newsletter(pk):
    # pk = self.kwargs.get('pk')
    # post = get_object_or_404(Post, pk=pk)
    post = Post.objects.get(pk=pk)
    categories = Category.objects.all()
    subscribers_emails = []
    author_email = post.author.user.email

    for cat in categories:
        subscribers = cat.subscribers.all()
        subscribers_emails += [s.email for s in subscribers if s.email != author_email]

    html_content = render_to_string(
        'account/email/post_email.html',
        {
            'small_text': post.preview(),
            'link': f'{settings.SITE_URL}/news/{post.pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=post.title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
# return redirect('/')

# ----------------------------------  task 3 --------------------------------


@shared_task()
def send_mail_every_monday8am():
    today = timezone.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_in__gte=last_week)
    categories = set(posts.values_list('categories_post__category_name', flat=True))
    subscribers = set(
        Category.objects.filter(category_name__in=categories).values_list('subscribers__email', flat=True))
    subscribers = list(filter(None, subscribers))  # удаляю пустое значение из списка ""

    html_content = render_to_string(
        'account/email/weekly.html',
        {
            'link': settings.SITE_URL + '/posts',
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Новости за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[subscribers],
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

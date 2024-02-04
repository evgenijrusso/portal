import datetime
import time
from celery import shared_task
from django.utils import timezone
# from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .models import Post, Category, User, Author


@shared_task
def hello():
    time.sleep(10)
    print('Hello, John')


# ----------------------------------  task 2 --------------------------------
@shared_task()
def send_newsletter():
    post_id = Post.objects.all().only('id').last().id
    # pk = self.kwargs.get('pk')
    # post = Post.objects.get(pk=pk)
    post = Post.objects.get(id=post_id)
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
        Category.objects.filter(category_name__in=categories).values_list('subscribers', flat=True))

    for user_id in subscribers:
        if user_id:
            user = User.objects.get(id=user_id)
#            print('user, user_emailб posts: ', user, user.email, posts)
        else:
            print('не подписчик')
        html_content = render_to_string(
            'account/email/weekly.html',
            {
                'link': f'{settings.SITE_URL}/news/',
                'posts': posts,
            }
        )

        msg = EmailMultiAlternatives(
            subject='Новости за неделю',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()

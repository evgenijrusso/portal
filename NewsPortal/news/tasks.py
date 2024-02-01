from celery import shared_task
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import time
from .models import Post, Category

@shared_task
def hello():
    time.sleep(10)
    print('Hello, John')


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

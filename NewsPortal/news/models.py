from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user, self.rating}'


class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)


class Post(models.Model):
    news = 'NE'
    articles = 'AR'

    TYPES = [
        (news, 'Новости'),
        (articles, 'Статьи')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    choice_types = models.CharField(max_length=2, choices=TYPES, default=news)
    time_in = models.DateTimeField(default=timezone.now) # time_in = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=250, default='')
    content = models.TextField(blank=False)
    rate_new = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title, self.rate_new}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(blank=False)
    comment_time_in = models.DateTimeField(timezone.now)
    comment_rate = models.IntegerField(default=0)

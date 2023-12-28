from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models import Sum
from django.db.models.functions import Coalesce


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        # рейтинг всех постов автора
        posts_rating = Post.objects.filter(author=self).aggregate(result=Coalesce(Sum('rate_new'),0)).get('result')

        # коммертарии автора
        comments_rating = Comment.objects.filter(user=self.user).aggregate(result=Coalesce(Sum('comment_rate'),0)).get('result')
        #  все комментарий к постам автора
        post_comment_rating = Comment.objects.filter(post__author=self).aggregate(result=Coalesce(Sum('comment_rate'),0)).get('result')

        print('pr: ', posts_rating)
        print('---------')
        print('cr: ', comments_rating)
        print('---------')
        print('pcr: ', post_comment_rating)

        self.rating = 3 * posts_rating + comments_rating  + post_comment_rating
        self.save()


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
    time_in = models.DateTimeField(default=timezone.now)  # models.DateTimeField(default=datetime.now)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=240, default='')
    content = models.TextField(blank=False)
    rate_new = models.IntegerField(default=0)

    def datatostr(self):
       # date_only = self.time_in.date()
        return self.time_in.strftime('%Y-%m-%d')

    def preview(self):
        if len(self.text_post) > 124:
            return self.text_post[:124] + '...'
        else:
            return self.text_post

    def like(self):
        self.rate_new += 1
        self.save()

    def dislike(self):
        self.rate_new -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(blank=False)
    comment_time_in = models.DateTimeField(default=timezone.now)
    comment_rate = models.IntegerField(default=0)

    def like(self):
        self.comment_rate += 1
        self.save()

    def dislike(self):
        self.comment_rate -= 1
        self.save()



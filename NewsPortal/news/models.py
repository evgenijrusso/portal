from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models import Sum


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        # рейтинг всех постов автора
        posts_rating = Post.objects.filter(author=self).aggregate(result=Sum('rate_new')).get('result')

        # коммертарии автора
        comments_rating = Comment.objects.filter(user=self).aggregate(result=Sum('comment_rate')).get('result')
        #  все комментарий к постам автора
        post_comment_rating = 0 #Comment.objects.filter(post__author=self.user).aggregate(result=Sum('comment_rate')).get('result') # ?

        print('pr: ', posts_rating)
        print('---------')
        print('cr: ', comments_rating)
        print('---------')
        print('pcr: ', post_comment_rating)

        self.rating = 3 * posts_rating + comments_rating  + post_comment_rating
     #   self.save()


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
    time_in = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=240, default='')
    content = models.TextField(blank=False)
    rate_new = models.IntegerField(default=0)

    def preview(self):
        return f'{self.content[:174]}...'

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



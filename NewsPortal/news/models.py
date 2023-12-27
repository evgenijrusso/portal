from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models import Sum


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        # рейтинг всех постов автора
        posts_rating = 0 # Post.objects.filter(author=self).aggregate(result=Sum('rate_new')).get('result')
        # коммертарии автора
        comments_rating = 0 # Comment.objects.filter(user=self).aggregate(result=Sum('comment_rate')).get('result')
        #  все комментарий к постам автора
        post_comment_rating = 0 # Comment.objects.filter(post__author__user=self.user).aggregate(result=Sum('rating')).get('result')

        posts = Post.objects.filter(author=self)  # публикации по текущему автору self-автор
        for p in posts:
            posts_rating += p.rating

        comments = Comment.objects.filter(user=self.user)     # список комментариев текущего автора
        for c in comments:
            comments_rating += c.rating
        post_comment = Comment.objects.filter(post_author=self)
        for pc in post_comment:
            post_comment_rating += pc.comments_rating

        print('')
        print('pr: ', posts_rating)
        print('cr: ', comments_rating)
        print('pcr: ', post_comment_rating)


        self.rating = posts_rating * 3 + comments_rating + post_comment_rating
        self.save()

        self.rating = 3 * posts_rating + comments_rating + post_comment_rating
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
    time_in = models.DateTimeField(default=timezone.now) # time_in = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=250, default='')
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



from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models import Sum
from django.db.models.functions import Coalesce


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username}'

    def get_user_categories(self):
        return list(self.user.categories.values_list("category_name"))
        # или self.user.categories.all()


    def update_rating(self):
        # рейтинг всех постов автора
        posts_rating = Post.objects.filter(author=self)\
            .aggregate(result=Coalesce(Sum('rate_new'), 0)).get('result')

        # коммертарии автора
        comments_rating = Comment.objects.filter(user=self.user)\
            .aggregate(result=Coalesce(Sum('comment_rate'), 0)).get('result')

        #  все комментарий к постам автора
        post_comment_rating = Comment.objects.filter(post__author=self)\
            .aggregate(result=Coalesce(Sum('comment_rate'), 0)).get('result')

        self.rating = 3 * posts_rating + comments_rating + post_comment_rating
        self.save()

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True, verbose_name='Category')
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return f'{self.category_name}'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.id})

    def get_subscribers(self):
        return list(self.subscribers.values_list("username"))

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



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
    categories_post = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=240, default='')
    content = models.TextField(blank=False)
    rate_new = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):  # 'pk' как в url.py, иначе не работает
        return reverse('post_detail', kwargs={'pk': self.id})


    def datatostr(self):
        return f"{self.time_in.strftime('%Y-%m-%d')}"

    def preview(self, length=124):
        return f"{self.content[:length]}..." if len(self.content) > length else self.content

    def get_categories_admin(self):
        return self.categories_post.values_list('category_name', flat=True).first() # для admin

    def get_categories_all(self):    # для signal.py
        return list(self.categories_post.all())

    def get_categories_post(self):    # для posts.html (вывод категории)
        return self.categories_post.all()[0]

    def get_post_author_user(self):
        return self.author.userall.username

    def like(self):
        self.rate_new += 1
        self.save()

    def dislike(self):
        self.rate_new -= 1
        self.save()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(blank=True)
    comment_time_in = models.DateTimeField(default=timezone.now)
    comment_rate = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.comment_text}'

    def like(self):
        self.comment_rate += 1
        self.save()

    def dislike(self):
        self.comment_rate -= 1
        self.save()

    def datatostr(self):
        return f"{self.comment_time_in.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

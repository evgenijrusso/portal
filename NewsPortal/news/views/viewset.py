import django_filters

from news.serializers import AuthorSerializer, CategorySerializer, ArticlesSerializer, NewsSerializer, UserSerializer
from rest_framework import viewsets, permissions
from rest_framework.reverse import reverse

from django.contrib.auth.models import User
from .author import Author
from .category import Category
from .post import Post


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class PostsViewset(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     filterset_fields = ["choice_types", "categories_post"]

class NewsViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(choice_types='NE')
    serializer_class = NewsSerializer

class ArticlesViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(choice_types='AR')
    serializer_class = ArticlesSerializer

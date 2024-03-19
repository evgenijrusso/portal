from .models import Post, Category, Author, User
from rest_framework import serializers


# class PostSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Post
#
#         fields = ['id', 'choice_types', 'time_in', 'categories_post', 'title', 'content', 'rate_new', 'url', ]
#         extra_kwargs = {
#             'url': {'view_name': 'post-detail', 'lookup_field': 'pk'}
#         }


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'choice_types', 'time_in', 'categories_post', 'title', 'content', 'rate_new', 'url', ]
        extra_kwargs = {
            'url': {'view_name': 'post-detail', 'lookup_field': 'pk'}
        }


class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'choice_types', 'time_in', 'categories_post', 'title', 'content', 'rate_new', 'url', ]
        # extra_kwargs = {
        #     'url': {'view_name': 'post-detail', 'lookup_field': 'pk'}
        # }


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'url', ]
        extra_kwargs = {
            'url': {'view_name': 'category-detail', 'lookup_field': 'pk'}
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', ]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'url', 'user', 'rating', ]
        extra_kwargs = {
            'url': {'view_name': 'author-detail', 'lookup_field': 'pk'}
        }
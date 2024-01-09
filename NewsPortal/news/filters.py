from django_filters import FilterSet
from .models import Post

# Создаем свой набор фильтров для модели Post. FilterSet, который мы наследуем,


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['icontains'],
            'time_in': ['exact', 'year__gt'],
        }

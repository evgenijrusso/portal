from django import forms
from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFilter, ChoiceFilter
from .models import Post, Author


class PostFilter(FilterSet):
    title = CharFilter(
        label='Содержит',
        lookup_expr='icontains'
    )
    author = ModelChoiceFilter(
        queryset=Author.objects.all(),
        lookup_expr='exact',
        label='Автор',
        empty_label='Все авторы',
    )
    time_in = DateFilter(
        label='Опубликованы после',
        lookup_expr='gt',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form'})
    )

    class Meta:
        model = Post
        fields = []



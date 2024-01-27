from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

from .models import Post


class PostForm(forms.ModelForm):
    title: forms.CharField(min_length=4, widget=forms.TextInput(attrs={'required': True}))
    content: forms.CharField(min_length=20, widget=forms.Textarea(attrs={'cols': 150, 'rows': 15}))

    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'categories_post', 'rate_new']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if content == title:
            raise ValidationError(
                'Текст не должен совпадать с заголовком.'
            )
        # не отрабатывает ошибку после 3-х попыток
        # author = cleaned_data.get('author')
        # today = date.today()  # текущий день
        # post_limit = Post.objects.filter(author=author, time_in__date=today).count()  # число возможных авторов
        # if post_limit >= 3:
        #     raise ValidationError('Нельзя публиковать больше 3-х постов в сутки')

        return cleaned_data


class CommonSignupForm(SignupForm):

    def save(self, request):
        # Ensure you call the parent class's save. Save() returns a User object.
        user = super(CommonSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user

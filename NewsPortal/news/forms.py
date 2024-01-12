from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    title: forms.CharField(min_length=4, widget=forms.TextInput(attrs={'required': True}))
    content: forms.CharField(min_length=20, widget=forms.Textarea({'cols': 50, 'rows': 5}))

    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'categories', 'rate_new']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if content == title:
            raise ValidationError(
                'Текст не должен совпадать с заголовком.'
            )

        return cleaned_data

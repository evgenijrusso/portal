from django.views.generic import ListView

from news.models import Author, User


APP = 'news/'


class AuthorList(ListView):
    model = Author
    ordering = '-rating'
    template_name = APP + 'authors.html'
    context_object_name = 'authors'
    queryset = Author.objects.all().select_related('user')


class UserList(ListView):
    model = User
    queryset = User.objects.all()

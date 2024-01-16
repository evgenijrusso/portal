from django.views.generic import ListView

from news.models import Author


APP = 'news/'


class AuthorList(ListView):
    model = Author
    ordering = '-rating'
    template_name = APP + 'authors.html'
    context_object_name = 'authors'

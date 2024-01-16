from django.views.generic import ListView

from news.models import Category


APP = 'news/'


class CategoryList(ListView):
    model = Category
    ordering = 'category_name'
    template_name = APP + 'categories.html'
    context_object_name = 'categories'

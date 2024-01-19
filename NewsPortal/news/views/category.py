from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from news.models import Category
from .post import PostList


APP = 'news/'


class CategoryList(ListView):
    model = Category
    ordering = 'category_name'
    template_name = APP + 'categories.html'
    context_object_name = 'categories'


class CategoryListView(PostList):
    template_name = APP + 'categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        # self.category = Category.obgects.filter().first(id='pk').only('id').first().id
        queryset = PostList.objects.filter(category=self.category).order_by('-time_in')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
     #   context['is_not_subcriber'] = self.request.user not in self.category

        return context

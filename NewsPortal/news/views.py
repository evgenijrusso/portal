from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import *
from .filters import PostFilter

APP = 'news/'


class AuthorList(ListView):
    model = Author
    ordering = '-rating'
    template_name = APP + 'authors.html'
    context_object_name = 'authors'


class CategoryList(ListView):
    model = Category
    ordering = 'category_name'
    template_name = APP + 'categories.html'
    context_object_name = 'categories'


class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = APP + 'posts.html'
    context_object_name = 'posts'
    paginate_by = 4


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


    # def get_ordering(self):
    #     ordering = self.request.GET.get('ordering', '-time_in')
    #     return ordering


class PostDetail(DetailView):
    model = Post
    template_name = APP + 'post.html'
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["now"] = timezone.now()
        return context


class CommentList(ListView):
    model = Comment
    ordering = 'comment_time_in'
    template_name = APP + 'comments.html'
    context_object_name = 'comments'


def index(request):
    return render(request, APP + 'index.html')



class PostSearch(ListView):
    model = Post
    ordering = '-time_in'
    template_name = APP + 'search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs    # Возвращаем из функции отфильтрованный список товаров

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

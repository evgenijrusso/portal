from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

app = 'news/'

class AuthorList(ListView):
    model = Author
    ordering = '-rating'
    template_name = app + 'authors.html'
    context_object_name = 'authors'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author.html'
    context_object_name = 'author'


class CategoryList(models.Model):
    model = Category
    ordering = 'category_name'
    template_name = 'categories.html'
    context_object_name = 'categories'


class PostList(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'posts.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class CommentList(ListView):
    model = Comment
    ordering = 'comment_time_in'
    template_name = 'comments.html'
    context_object_name = 'comments'


class CommentDetail(DetailView):
    model = Comment
    template_name = 'comment.html'
    context_object_name = 'comment'


# class Proba(View):
#     def get(self, request, cat_slug):
#         categories = Category.objects.all()
#         context = {'categories': categories, 'title': 'Главная страница'}
#         return render(request, "news/about.html")


def default(request):
    return render(request, app + "default.html")

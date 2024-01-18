from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView, TemplateView

from news.models import *
from news.forms import PostForm
from news.filters import PostFilter

APP = 'news/'


class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = APP + 'posts.html'
    context_object_name = 'posts'
    paginate_by = 4


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список постов'
        return context


class PostDetail(DetailView):
    model = Post
    template_name = APP + 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пост'
        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = APP + 'post_edit.html'
    success_url = '/news/'
    permission_required = ('news.add_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/articles/create/':
            post.choice_types = 'AR'
        post.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get_title'] = self.get_type_create()[0]
        context['get_create_update'] = self.get_type_create()[1]
        return context

    def get_type_create(self):
        if self.request.path == '/news/articles/create/':
            return ['Create article', 'Добавить статью']
        else:
            return ['Create news', 'Добавить новость']


class PostUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = APP + 'post_edit.html'
    success_url = reverse_lazy('posts')
    permission_required = ('news.change_post',)
  #  redirect_field_name = '/'

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_autenticated:
    #         return self.handle_no_permission()
    #     return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get_title'] = self.get_type_update()[0]
        context['get_create_update'] = self.get_type_update()[1]
        return context

    def get_type_update(self):
        if 'articles' in self.request.path:      # здесь появляется неверный адрес
            return ['Edit article', 'Редактировать статью']
        else:
            return ['Edit news', 'Редактировать новость']


class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = APP + 'post_delete.html'
    success_url = reverse_lazy('posts')
    permission_required = ('news.delete_post',)

# ----------------------------  post  search ------------------------
class PostSearch(ListView):
    model = Post
    ordering = '-time_in'
    template_name = APP + 'search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs  # Возвращаем из функции отфильтрованный список товаров

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import *
from .forms import PostForm
from .filters import PostFilter

APP = 'news/'


class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = APP + 'posts.html'
    context_object_name = 'posts'
    paginate_by = 4


class PostDetail(DetailView):
    model = Post
    template_name = APP + 'post_detail.html'
    context_object_name = 'post'


class PostNewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = APP + 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/create/':
            post.type = 'NE'
        post.save()
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = APP + 'post_edit.html'
    success_url = reverse_lazy('posts')


class PostDelete(DeleteView):
    model = Post
    template_name = APP + 'post_delete.html'
    success_url = reverse_lazy('posts')

    # def get_queryset(self):
    #     owner = self.request.author.user
    #     return self.model.objects.filter(owner=owner)
# ------------------------------------------------------------------


def index(request):
    return render(request, APP + 'index.html')


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


class CommentList(ListView):
    model = Comment
    ordering = 'comment_time_in'
    template_name = APP + 'comments.html'
    context_object_name = 'comments'


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

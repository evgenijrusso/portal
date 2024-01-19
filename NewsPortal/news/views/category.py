from django.contrib.auth.decorators import login_required
#from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.shortcuts import render

from news.models import Category
from .post import PostList


APP = 'news/'


class CategoryList(ListView):
    model = Category
    template_name = APP + 'categories.html'
    context_object_name = 'category_list'

#     def get_queryset(self):
#         self.category = get_object_or_404(Category, id=self.kwargs['pk'])
#         # self.category = Category.obgects.filter(pk ='pk').only('id').first().id
#         queryset = PostList.objects.filter(category=self.category).order_by('-time_in')
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['is_not_subcriber'] = self.request.user not in self.category.subscribers.all()
#         context['category'] = self.category
#         return context
#
# @login_required
# def subscribe(request, pk):
#     user = request.user
#     category = Category.objects.get(id=pk)
#     category.subscribers.add(user)
#
#     messsage = 'Вы успешно подписались на рассылку новостей категории'
#     return render(request, 'news/subscribe.html', {'category': category, 'messsage': messsage})


# category.html
#  for post in category_new_list
#   <a href="{% url "post_detail" post.id %}> {{ post.title}}</a>
#   <a href="{% url "post_update" post.id %}> Редактировать</a>
#   <a href="{% url "post_delete" post.id %}> Удалить</a>

# {% for category in post.category.all %}
# <a href="{%  url "categories" category.id  %}"> {{ category}<a/>

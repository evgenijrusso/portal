from django.urls import path
from news.views.post import PostList, PostDetail, PostCreate, \
    PostDelete, PostUpdate, PostSearch
from allauth.account.views import SignupView, LoginView, LogoutView

from news.views.author import AuthorList
from news.views.category import CategoryList
from news.views.comment import CommentList
from news.views.index import index
from news.views.profile import ProfileView, upgrade_to_author


class MySignupView(SignupView):
    template_name = 'signup.html'


class MyLoginView(LoginView):
    template_name = 'login.html'


class MyLogoutView(LogoutView):
    template_name = 'logout.html'


urlpatterns = [
    path('', index),  # http://127.0.0.1:8004
    path('news/', PostList.as_view(), name='posts'),
    path('news/articles/', PostList.as_view(), name='articles'),
    path('news/create/', PostCreate.as_view(), name='posts_news_create'),
    path('news/articles/create/', PostCreate.as_view(), name='posts_articles_create'),
    path('news/search/', PostSearch.as_view(), name='post_search'),
    path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('news/articles/<int:pk>/edit/', PostUpdate.as_view(), name='posts_articles_edit'),
    #path('news/categories/<int:pk>')

    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/upgrade/', upgrade_to_author, name='upgrade_to_author'),

    path('accounts/signup/', MySignupView.as_view(), name='signup'),
    path('accounts/login/', MyLoginView.as_view(), name='login'),
    path('accounts/logout/', MyLogoutView.as_view(), name='logout'),

    path('authors/', AuthorList.as_view(), name='authors'),
    path('comments/', CommentList.as_view(), name='comments'),
    path('categories/', CategoryList.as_view(), name='categories'),
]


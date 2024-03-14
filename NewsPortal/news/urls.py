from django.urls import path

from news.views.post import PostList, PostDetail, PostCreate, PostDelete, PostUpdate, PostSearch
from news.views.author import AuthorList
from news.views.category import CategoryListView, CategoryDetailView, subscribe, unsubscribe
from news.views.comment import CommentList
from news.views.index import Index
from news.views.profile import ProfileView, upgrade_to_author


urlpatterns = [
    path('', Index.as_view(), name='index'),  # http://127.0.0.1:8004
    path('news/', PostList.as_view(), name='posts'),
    path('news/articles/', PostList.as_view(), name='articles'),
    path('news/create/', PostCreate.as_view(), name='posts_news_create'),
    path('news/articles/create/', PostCreate.as_view(), name='posts_articles_create'),
    path('news/search/', PostSearch.as_view(), name='post_search'),
    path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('news/articles/<int:pk>/edit/', PostUpdate.as_view(), name='posts_articles_edit'),


    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/upgrade/', upgrade_to_author, name='upgrade_to_author'),
    path('accounts/', Index.as_view(), name='index'),  # http://127.0.0.1:8004/accounts
#    path('accounts/google', index),  # http://127.0.0.1:8004/accounts


    path('authors/', AuthorList.as_view(), name='authors'),
    path('comments/', CommentList.as_view(), name='comments'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
    path('categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),


]


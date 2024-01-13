from django.urls import path
from .views import AuthorList, CategoryList, PostList, PostDetail, PostCreate, \
    PostDelete, PostUpdate, CommentList, index, PostSearch


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

    path('authors/', AuthorList.as_view(), name='authors'),
    path('comments/', CommentList.as_view(), name='comments'),
    path('categories/', CategoryList.as_view(), name='categories'),

]

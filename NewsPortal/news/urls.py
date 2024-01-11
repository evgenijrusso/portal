from django.urls import path
from .views import AuthorList, CategoryList, PostList, PostDetail, PostNewsCreate, \
    PostDelete, PostUpdate, CommentList, index, PostSearch


urlpatterns = [
    path('', index),  # http://127.0.0.1:8004
    path('news/', PostList.as_view(), name='posts'),
    path('news/create/', PostNewsCreate.as_view(), name='posts_news_create'),  # PostNewsCreate  PostArticlesCreate
    path('news/search/', PostSearch.as_view(), name='post_search'),
    path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('news/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),

    path('authors/', AuthorList.as_view(), name='authors'),
    path('comments/', CommentList.as_view(), name='comments'),
    path('categories/', CategoryList.as_view(), name='categories'),

]

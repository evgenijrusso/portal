from django.urls import path
from .views import AuthorList, CategoryList, PostList, PostDetail, CommentList


urlpatterns = [

    path('', PostList.as_view(), name='posts'),  # http://127.0.0.1:8004
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('authors/', AuthorList.as_view(), name='authors'),
    path('comments/', CommentList.as_view(), name='comments'),
    path('categories/', CategoryList.as_view(), name='categories'),

]

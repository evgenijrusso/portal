from django.urls import path
from .views import AuthorList, AuthorDetail, default

urlpatterns = [
    path('', default),  # http://127.0.0.1:8004
    path('authors/', AuthorList.as_view(), name='authors'),
    path('<int:pk>', AuthorDetail.as_view(), name='author'),
#    path('about/', default, name='default'),
]

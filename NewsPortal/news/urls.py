from django.urls import path
from .views import AuthorList, AuthorDetail, default

urlpatterns = [
    path('authors/', AuthorList.as_view()),  #name='authors'
    path('<int:pk>', AuthorDetail.as_view()),
    path('about/', default, name='default'),
]

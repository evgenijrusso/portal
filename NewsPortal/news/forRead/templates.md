Вопросы по templates
---------------------

1-й вариант  `settings.py`  
-------------------------------------
'DIRS': [os.path.join(BASE_DIR, 'templates')],

`work/urls.py`:
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls'))
]
```
`news/urls.py`
```
from django.urls import path
from .views import AuthorList, AuthorDetail, default

urlpatterns = [
    path('authors/', AuthorList.as_view()),  #name='authors'
    path('<int:pk>', AuthorDetail.as_view()),
    path('about/', default, name='default'),
]
```
`views.py`
```
app = 'news/' 
def default(request):
    return render(request, app + "default.html")
```

2-й вариант  `settings.py`  
-------------------------------------
'DIRS': [BASE_DIR / 'news' / 'templates'],
То же самое, что в 1-ом варианте
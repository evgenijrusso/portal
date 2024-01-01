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

3-й вариант  `settings.py`  
-------------------------------------
'DIRS': [BASE_DIR / 'news' / 'templates' / 'news'],
Во `views.py` можно удалить app = 'news/'

Подключение статических файлов
------------------------------
`STATIC_URL = 'static/'` - префикс url-адреса для статических файлов

`STATIC_ROOT = os.path.join(BASE_DIR, 'static/')`
путь к общей статической папке, формируемой при запуске командой `collectstatic` 
(для сбора всей статики в единый каталог при размещение сайта на реальном веб-сервере)

STATICFILES_DIRS = [BASE_DIR / 'news' / 'static'] - список дополнительных 
(нестандартных) путей к статическим файлам, используемых для сбора и для режима отладки.

Есть проблема с основным url. Оказывается, что нужно разместить еще один `templates` в 
корне проекта. И там разместить дефолтный шаблон html.

`news/urls.py`
Надо было так! `path('news/', default),  # http://127.0.0.1:8004`
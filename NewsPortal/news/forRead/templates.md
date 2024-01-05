Вопросы по templates
---------------------

`settings.py`  
-------------------------------------
'DIRS': [os.path.join(BASE_DIR, 'templates')],

`work/urls.py`:
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('news.urls'))
]
```


Подключение статических файлов
------------------------------
`STATIC_URL = 'static/'` - префикс url-адреса для статических файлов

`STATIC_ROOT = os.path.join(BASE_DIR, 'static/')`
путь к общей статической папке, формируемой при запуске командой `collectstatic` 
(для сбора всей статики в единый каталог при размещение сайта на реальном веб-сервере)

STATICFILES_DIRS = [BASE_DIR / 'news' / 'static'] - список дополнительных 
(нестандартных) путей к статическим файлам, используемых для сбора и для режима отладки.
p.s. Пока гн стал устанавливать


default.html
-------------
Оказывается, что нужно разместить еще один `templates` в корне проекта. И там разместить 
дефолтный шаблон html.

Следует обратить внимание на идентичность записи href="":
<li class="nav-item"><a class="nav-link" href="/categories/">Categories</a></li>
<li class="nav-item"><a class="nav-link" href="{% url 'main' %}">News</a></li>
p.s. Только в 1-ой записи обязательно должно быть 2 слеша ! ("/categories/")

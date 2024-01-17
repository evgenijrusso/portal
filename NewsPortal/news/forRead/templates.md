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

Временная проверка:
```
<li class="nav-item active">
    {% if user.is_authenticated %}
        <a class="nav-link">{{ request.user.username }}</a>
    {% endif %}
</li>
<li class="nav-item active">
    {% if not user.is_authenticated %}
        <a class="nav-link" href='{% url "account_login" %}'>Войти</a>
    {% endif %}
</li>
<li class="nav-item active">
    {% if not user.is_authenticated %}
        <a class="nav-link" href='{% url "account_signup" %}'>Регистрация</a>
    {% endif %}
</li>
<li class="nav-item active">
    {% if user.is_authenticated %}
        <a class="nav-link" href='{% url "account_logout" %}'>Выйти</a>
    {% endif %}
</li>
```
first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': ('First name')}))
last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': _'Last name')}))
    

 def custom_signup(self, request, user):
        # Ensure you call the parent class's save. Save() returns a User object.
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


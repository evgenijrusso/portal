Заметки по проекту
------------------
Админ: admin-1


p.s.  Авторы здесь были не нужны, достаточно пользователей. Про авторов в неделььной 
рассылке не было информации. Поэтому часть кода убрал.
```
for user_id in subscribers:
   if user_id:
        user = User.objects.get(id=user_id)
        is_user_author = Author.objects.filter(user_id=user_id).exists()
        print('user, user_email: ', user, user.email)
        print('posts:', posts)
        if is_user_author:
            posts_ = posts
            print(posts_)
            posts_ = set(posts.exclude(author=user.author))
            print(posts_)
        else:
            print('не автор')

        else:
            print('не подписчик')
```

   # subscribers = list(filter(None, subscribers))  # удаляю пустое значение из списка ""
   # subscribers = ('rasen800@gmail.com', 'preobrazhensky.evgenii@yandex.ru') #  'evgenijrusso@yandex.ru'

# ------------------------- Безопасность -----------------------  

И более того, Django содержит один полезный инструмент для проверки безопасности вашего приложения 
на основные угрозы.

Из корня приложения можно запустить команду:

`python3 manage.py check --deploy`

Результатом её выполнения является анализ приложения на наличие ошибок, угроз безопасности и др. 
Использование этой команды может быть также полезным при рассмотрении вашего приложения с точки 
зрения безопасности.

Результат проверки:
WARNINGS:
 a load balancer or reverse-proxy server to redirect all connections to HTTPS.
?: (security.W009) Your SECRET_KEY has less than 50 characters, less than 5 unique characters, or it's prefixed with 'django-insecure-' indicating that it was generated automatically by Django. Please gene
rate a long and random value, otherwise many of Django's security-critical features will be vulnerable to attack.
?: (security.W012) SESSION_COOKIE_SECURE is not set to True. Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
?: (security.W016) You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE, but you have not set CSRF_COOKIE_SECURE to True. Using a secure-only CSRF cookie makes it more difficult for netw
ork traffic sniffers to steal the CSRF token.
?: (security.W018) You should not have DEBUG set to True in deployment.
?: (security.W020) ALLOWED_HOSTS must not be empty in deployment.

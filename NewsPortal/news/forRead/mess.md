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

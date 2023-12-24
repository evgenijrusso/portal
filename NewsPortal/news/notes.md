Замечания по приложению `news`
------------------------------
# from news.models import Author, Post, Category, PostCategory, Comment
# from django.contrib.auth.models import User

* Создал двух пользователей (rasen, john)
    > u1 = User.objects.create_user(username='rasen')  
     u2 = User.objects.create_user('john')        
     u1.get_username -- `rasen` 

* Создать два объекта модели 'Author', связанные с пользователями.

a1 = Author.objects.create(author=u1)
a2 = Author.object.create(author.id=u1.id)

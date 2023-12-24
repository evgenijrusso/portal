Замечания по приложению `news`
------------------------------
* Создал двух пользователей (rasen, john)
    > u1 = User.objects.create_user(username='rasen')  
     u2 = User.objects.create_user('john')        
     u1.get_username() -- `rasen` 

* Создать два объекта модели 'Author', связанные с пользователями.

user1 = User.objects.create_user(username='rasen')
author1 = Author.objects.create(author=u1)
author1 = Author.object.create(author.id=u1.id)

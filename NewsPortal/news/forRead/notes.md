Замечания по приложению `news`
------------------------------
 
>1. Создал 3-х пользователей (rasen, john, peter)   
u1 = User.objects.create_user(username='rasen')      
u2 = User.objects.create_user('john')        
u3 = User.objects.create_user('peter')

>2. Создал два объекта модели 'Author', связанные с пользователями.  
a1 = Author.objects.create(user=u1)   
a2 = Author.objects.create(user=u2) 

>3. Добавил 4 категории в модель Category.
c1 = Category.objects.create(category_name='Спорт')  
c2 = Category.objects.create(category_name='Политика')  
c3 = Category.objects.create(category_name='Образование')   
c4 = Category.objects.create(category_name='Медицина')    
 
>4. Добавил 2 статьи и 1 новость.   
p1 = Post.objects.create(author=a1, choice_types='AR')  
p2 = Post.objects.create(author=a2, choice_types='AR')  
p3 = Post.objects.create(author=a2, choice_types='NE') 

>5. Присвоить им категории (как минимум в одной 
статье/новости должно быть не меньше 2 категорий).   
pc1 = PostCategory.objects.create(category=c1, post=p1)  
pc2 = PostCategory.objects.create(category=c2, post=p2)  
pc3 = PostCategory.objects.create(category=c3, post=p3)     

>6. Создать как минимум 4 комментария к разным объектам  
модели Post (в каждом объекте должен быть как минимум один комментарий).     
com1 = Comment.objects.create(post=p1, user=a1.user, comment_text='се ля ви')  
com2 = Comment.objects.create(post=p2, user=a2.user, comment_text='все возможно')  
com3 = Comment.objects.create(post=p3, user=a2.user, comment_text='волейбол')  
 
>7. Коррекция рейтингов в Post и Comment 
p1.like()  
p2.dislike() 
p2.like()  
p3.like() 
p3.dislike()
com1.like()  
com2.like()
com2.dislike()
com3.dislike()

>8. Обновить рейтинги пользователей.
a1.rating = 34 a1.save()
a2.rating = 4 a1.save()
a1.update_rating() - 34
a2.update_rating() - 4

>9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
Author.objects.order_by('-rating').values('rating', 'user').first()
-- Out[20]: {'rating': 34, 'user': 1}



>10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, 
основываясь на лайках/дислайках к этой статье.

Post.objects.all().order_by('-rate_new').values('time_in', 'author__user__username', 'rate_new', 'title', 'content')[0]

Out[15]: 
{'time_in': datetime.datetime(2023, 12, 24, 14, 19, 6, 197172, tzinfo=datetime.timezone.utc),
 'author__user__username': 'rasen',
 'rate_new': 8,
 'title': 'Весна',
 'content': 'Солнце пригрело. Побежал ручьи. Прилетели грачи. Птицы выводят птенцов. Весело скачет по лесу заяц. 
Лисица вышла на охоту и чует добычу. Волчица вывела волчат на поляну. Медведица рычит у берлоги. 
Над цветами летают бабочки и пчелы. Все рады весне.'}

>

Comment.objects.all().order_by().values('time_in', 'user__username', 'comment_rate', 'comment_text')[0]



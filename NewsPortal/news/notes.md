Замечания по приложению `news`
------------------------------
# from news.models import Author, Post, Comment, Category, PostCategory  
from django.contrib.auth.models import User
from django.db.models import Max, Sum
from news.models import *

- u1.get_username -- `rasen` 
- u1 = User.objects.get(username='rasen')
- u1 = User.objects.get(pk=1)

> Создал двух пользователей (rasen, john)   
u1 = User.objects.create_user(username='rasen')      
u2 = User.objects.create_user('john')        
u3 = User.objects.create_user('peter')
> 
> Создал два объекта модели 'Author', связанные с пользователями.  
a1 = Author.objects.create(user=u1)  
a2 = Author.objects.create(user=u2)

a1 = Author.objects.get(pk=2)

> Добавил 4 категории в модель Category.
c1 = Category.objects.create(category_name='Спорт')
c2 = Category.objects.create(category_name='Политика')
c3 = Category.objects.create(category_name='Образование')
c4 = Category.objects.create(category_name='Медицина') 
 
> Добавил 2 статьи и 1 новость.   
p1 = Post.objects.create(author=a1, choice_types='AR')  
p2 = Post.objects.create(author=a2, choice_types='AR')  
p3 = Post.objects.create(author=a2, choice_types='NE') 

> Присвоить им категории (как минимум в одной 
статье/новости должно быть не меньше 2 категорий).   
pc1 = PostCategory.objects.create(category=c1, post=p1)  
pc2 = PostCategory.objects.create(category=c2, post=p2)  
pc3 = PostCategory.objects.create(category=c3, post=p3)     

> Создать как минимум 4 комментария к разным объектам  
модели Post (в каждом объекте должен быть как минимум один комментарий).     
com1 = Comment.objects.create(post=p1, user=a1.user, comment_text='се ля ви')  
com2 = Comment.objects.create(post=p2, user=a2.user, comment_text='все возможно')  
com3 = Comment.objects.create(post=p3, user=a2.user, comment_text='волейбол')  
 

>Коррекция рейтингов в Post 
p1.like()  
p2.dislike() 
p2.like()  
p3.like() 
p3.dislike()

>Коррекция рейтингов в Comment 
com1.like()  
com2.like()
com2.dislike()
com3.dislike()



>Обновить рейтинги пользователей.
a1.rating = 5 a1.save()
a2.rating = 3 a1.save()
Author.update_rating(a1) - 15
Author.update_rating(a1) - 9

> Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
Author.objects.order_by('-rating').first()   result: <Author: (<User: rasen>, 5)>
Author.objects.order_by('-rating').values('rating').first()  result: {'rating': 5}

> Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, 
основываясь на лайках/дислайках к этой статье.
 



----------------- Тест по  сортировке ----------------------------
Author.objects.all().order_by('rating') - <QuerySet [<Author: (<User: john>, 3)>, <Author: (<User: rasen>, 5)>]>
Author.objects.order_by('-rating') <QuerySet [<Author: (<User: rasen>, 5)>, <Author: (<User: john>, 3)>]>
Author.objects.order_by('-rating').values('rating')  <QuerySet [{'rating': 5}, {'rating': 3}]>
Author.objects.order_by('-rating').values_list('rating') <QuerySet [(5,), (3,)]>
Author.objects.order_by('-rating').values_list('rating', flat=True) <QuerySet [5, 3]>

Author.objects.aggregate(Max('rating')) - {'rating__max': 5}
Author.objects.order_by('-rating').first() <Author: (<User: rasen>, 5)>
----------------------------------------------------------------------------------------
a1=Author.objects.get(pk=2) - <Author: (<User: rasen>, 5)>
a2=Author.objects.get(pk=3) <Author: (<User: john>, 3)>

posts_rating = Post.objects.filter(author=a1).aggregate(result=Sum('rate_new')).get('result')    
result: posts_rating = 3 
posts_rating = Post.objects.filter(author=a2).aggregate(result=Sum('rate_new')).get('result')
result: posts_rating = 1

u1 = User.objects.get(pk=1) <User: rasen>
comments_rating = Comment.objects.filter(user=a1.user).aggregate(result=Sum('comment_rate')).get('result')   
u2 = User.objects.get(pk=2)  <User: john>
comments_rating = Comment.objects.filter(user=a2.user).aggregate(result=Sum('comment_rate')).get('result')   
u3 = User.objects.get(pk=3)  <User: peter>
comments_rating = Comment.objects.filter(user=a3.user).aggregate(result=Sum('comment_rate')).get('result')   

=============================
from django.contrib.auth.models import User
from news.models import *
u1 = User.objects.get(pk=1)
u2 = User.objects.get(pk=2)
a1 = Author.objects.get(pk=2)
a2 = Author.objects.get(pk=3)
p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)
com1 = Comment.objects.get(pk=1)
com2 = Comment.objects.get(pk=2)
com3 = Comment.objects.get(pk=3)
a1.update_rating()  
a2.update_rating()

========================







### Ускорение работы с 'Console shell'

```
from django.contrib.auth.models import User
from news.models import *
from django.db.models import Max, Sum
from django.db.models.functions import Coalesce

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
```

> Информация о пользователе 
    u1.get_username -- `rasen`  
    u1 = User.objects.get(username='rasen') 
    u1 = User.objects.get(pk=1) 
    u1 = User.objects.get(id=1)

> Информация о авторе
a1 = Author.objects.get(pk=2)    
a2 = Author.objects.get(pk=3)

> Обновление рейтинга (варианты) 
Author.update_rating(a1) 
Author.update_rating(a2)
a1.update_rating() - 34
a2.update_rating() - 4

Обратные отношения (Другой вариант)
-----------------------------------
Использование менеджера обратных отношений (_set) 
a1.post_set.all()
a1.post_set.all().values_list('id', flat=True)
a1.post_set.all().values_list('id','title')  -- Out[8]: <QuerySet [(1, 'Весна')]>
a1.comment_set.all().values_list('id','comment_text') -- AttributeError: 'Author' object has no attribute 'comment_set'
a1.user.comment_set.all().values_list('id','comment_text') -- Out[10]: <QuerySet [(1, 'се ля ви')]>

Пример:
# менеджер objects
posts_rating = Post.objects.filter(author=self).aggregate(result=Coalesce(Sum('rate_new'),0)).get('result')
# через менеджер отношений
posts_rating = self.post_set.aggregate(result=Sum('rate_new')).get('result') 
comments_rating = self.user.comment_set.aggregate(result=Coalesce(Sum('comment_rate'),0)).get('result')
post_comment_rating = self.post_set.aggregate(result=Coalesce(Sum('comment_rate'),0)).get('result')

#  переопределение стандрартного менеджера отношений на пользовательский менеджер (related_name=)
author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts') -- Class Post  
user = models.ForeignKey(User, on_delete=models.CASCADE, , related_name='comments')   -- Class Comment
# Тогда меняем (пример)
posts_rating = self.post_set.aggregate(result=Sum('rate_new')).get('result')  -- прежнее решение 
posts_rating = self.posts.aggregate(result=Sum('rate_new')).get('result')   -- новое решение


Тест по  сортировке 
----------------------------
Author.objects.all().order_by('rating') - <QuerySet [<Author: (<User: john>, 3)>, <Author: (<User: rasen>, 5)>]>
Author.objects.order_by('-rating') <QuerySet [<Author: (<User: rasen>, 5)>, <Author: (<User: john>, 3)>]>
Author.objects.order_by('-rating').values('rating')  <QuerySet [{'rating': 5}, {'rating': 3}]>
Author.objects.order_by('-rating').values_list('rating') <QuerySet [(5,), (3,)]>
Author.objects.order_by('-rating').values_list('rating', flat=True) <QuerySet [5, 3]>

Author.objects.aggregate(Max('rating')) - {'rating__max': 5}
Author.objects.order_by('-rating').first() <Author: (<User: rasen>, 5)>

Тренировка
------------
a1=Author.objects.get(pk=2) - <Author: (<User: rasen>, 5)>
a2=Author.objects.get(pk=3) <Author: (<User: john>, 3)>

posts_rating = Post.objects.filter(author=a1).aggregate(result=Sum('rate_new')).get('result')    
result: posts_rating = 3 
posts_rating = Post.objects.filter(author=a2).aggregate(result=Sum('rate_new')).get('result')
result: posts_rating = 1

u1 = User.objects.get(pk=1) <User: rasen>
posts_rating = Post.objects.filter(author=self).aggregate(result=Coalesce(Sum('rate_new'),0)).get('result')
u2 = User.objects.get(pk=2)  <User: john>
comments_rating = Comment.objects.filter(user=self.user).aggregate(result=Coalesce(Sum('comment_rate'),0)).get('result')
u3 = User.objects.get(pk=3)  <User: peter>
post_comment_rating = Comment.objects.filter(post__author=self).aggregate(result=Coalesce(Sum('comment_rate'),0)).get('result')   

Вывод дата обновления, автора статьи,  рейтинг, заголовок и превью лучшей статьи
-------------------------------------------------------------------------------
Текст:
К сожалению, preview - это метод, а не поле, поэтому его не получиться разместить в запросе 
вместе с полями.
Можно по отдельности:
posts = Post.objects.order_by('-rate_new')
best_post = posts.values('time_in', 'author__user__username', 'rate_new', 'title').first()
best_preview = posts.first().preview() 

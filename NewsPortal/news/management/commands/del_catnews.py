from django.core.management.base import BaseCommand, CommandError
from news.models import Category, Post


class Command(BaseCommand):
    help = 'Удаление всех новостей из какой-либо категории "Временно"'

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Do you really want to Вelete a posts in one category ? yes/no')
        answer = input()

        if answer == 'yes':
            cat = Category.objects.get(category_name='Временно').id
            cat_posts = Post.objects.filter(categories_post=cat)
            if cat_posts.count() > 0:
                for post in cat_posts:
                    post.delete()
                    self.stdout.write(self.style.SUCCESS('Success detete posts from category "%s"' % str(post)))
            else:
                self.stdout.write(self.style.ERROR('Info, no posts'))
            return
        else:
            self.stdout.write(self.style.ERROR('Access denied'))

from django.core.management.base import BaseCommand
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Удаление всех новостей из выбранной категории'

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, help='Указывает на название категории')

    def handle(self, *args, **options):
        self.stdout.write(f'Вы хотите удалить все статьи в категории "{options["name"]}"? yes/no')
        answer = input()

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            name = Category.objects.get(category_name=options['name'])
            cat_posts = Post.objects.filter(categories_post=name).delete()
            if cat_posts[0] != 0:
                self.stdout.write(f'result { cat_posts }')
                self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {name}'))
            else:
                self.stdout.write(self.style.ERROR('Info, no posts'))
            return
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category'), {})

# Generated by Django 5.0 on 2024-03-11 12:21

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_alter_category_category_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Коммертарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='author',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Имя категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_rate',
            field=models.IntegerField(default=0, verbose_name='Рейтинг коммертария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(blank=True, verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_time_in',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='choice_types',
            field=models.CharField(choices=[('NE', 'Новости'), ('AR', 'Статьи')], default='NE', max_length=2, verbose_name='Выбор типа'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Контекст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rate_new',
            field=models.IntegerField(default=0, verbose_name='Новый рейтинг'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_in',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Часовой пояс'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=240, verbose_name='Заголовок'),
        ),
    ]
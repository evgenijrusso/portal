# Generated by Django 5.0.1 on 2024-03-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_alter_author_rating_alter_author_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Name of category'),
        ),
    ]
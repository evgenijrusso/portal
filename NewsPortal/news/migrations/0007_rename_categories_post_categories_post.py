# Generated by Django 5.0.1 on 2024-01-19 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_category_subscribers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='categories_post',
        ),
    ]

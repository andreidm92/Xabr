# Generated by Django 3.1 on 2021-01-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_post_posts_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
    ]
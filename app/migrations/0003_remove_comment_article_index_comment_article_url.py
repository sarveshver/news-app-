# Generated by Django 5.0 on 2023-12-08 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comment_article_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article_index',
        ),
        migrations.AddField(
            model_name='comment',
            name='article_url',
            field=models.URLField(null=True),
        ),
    ]

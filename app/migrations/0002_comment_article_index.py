# Generated by Django 5.0 on 2023-12-08 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article_index',
            field=models.IntegerField(null=True),
        ),
    ]

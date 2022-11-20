# Generated by Django 3.2.13 on 2022-11-20 03:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_movie_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like_users',
            field=models.ManyToManyField(related_name='like_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='like_users',
            field=models.ManyToManyField(related_name='like_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]

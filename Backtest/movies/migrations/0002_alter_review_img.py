# Generated by Django 3.2.13 on 2022-11-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='img',
            field=models.ImageField(default='', upload_to='%Y/%m/%d/'),
        ),
    ]

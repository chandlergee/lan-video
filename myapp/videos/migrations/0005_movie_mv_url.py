# Generated by Django 3.2.8 on 2021-10-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_alter_movie_mv_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='mv_url',
            field=models.CharField(default='', max_length=256, verbose_name='播放链接'),
        ),
    ]

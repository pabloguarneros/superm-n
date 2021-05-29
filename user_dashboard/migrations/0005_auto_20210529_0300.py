# Generated by Django 3.2 on 2021-05-29 03:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0004_manly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotion_schedule',
            name='emotions',
            field=models.ManyToManyField(blank=True, to='user_dashboard.Emotion'),
        ),
        migrations.AlterField(
            model_name='friend_list',
            name='emotions',
            field=models.ManyToManyField(blank=True, to='user_dashboard.Friend'),
        ),
        migrations.AlterField(
            model_name='manly',
            name='users_done',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

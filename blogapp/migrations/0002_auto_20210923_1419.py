# Generated by Django 3.2.6 on 2021-09-23 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='like_count',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='likes_user',
        ),
    ]
# Generated by Django 3.2.6 on 2021-09-23 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='like_posts',
        ),
    ]

# Generated by Django 3.2.6 on 2021-09-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_rename_commnet_text_comment_comment_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='hashtag',
            field=models.ManyToManyField(to='blogapp.HashTag'),
        ),
    ]
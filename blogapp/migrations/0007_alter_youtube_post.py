# Generated by Django 3.2.6 on 2021-09-15 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_youtube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='youtubes', to='blogapp.blog'),
        ),
    ]
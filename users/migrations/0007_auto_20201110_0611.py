# Generated by Django 3.0.8 on 2020-11-10 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201110_0555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='curr_sem',
        ),
        migrations.AddField(
            model_name='elective',
            name='approved',
            field=models.BooleanField(default='False'),
        ),
    ]

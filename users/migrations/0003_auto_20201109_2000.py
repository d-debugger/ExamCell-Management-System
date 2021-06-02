# Generated by Django 3.0.8 on 2020-11-09 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201109_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='net_sgpi',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
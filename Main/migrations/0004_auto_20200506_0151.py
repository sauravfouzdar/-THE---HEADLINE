# Generated by Django 3.0.5 on 2020-05-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200506_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='fb',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='tw',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='yut',
            field=models.TextField(default='-'),
        ),
    ]

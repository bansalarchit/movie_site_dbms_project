# Generated by Django 3.1.7 on 2021-12-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20211207_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]

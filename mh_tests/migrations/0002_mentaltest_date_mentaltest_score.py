# Generated by Django 4.1 on 2022-10-30 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mh_tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentaltest',
            name='date',
            field=models.DateTimeField(default=datetime.date(2022, 10, 30)),
        ),
        migrations.AddField(
            model_name='mentaltest',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]

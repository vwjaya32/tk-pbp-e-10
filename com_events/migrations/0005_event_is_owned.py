# Generated by Django 4.1 on 2022-10-29 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_events', '0004_event_is_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_owned',
            field=models.BooleanField(default=False),
        ),
    ]

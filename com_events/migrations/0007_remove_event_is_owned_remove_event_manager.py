# Generated by Django 4.1 on 2022-11-01 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('com_events', '0006_alter_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='is_owned',
        ),
        migrations.RemoveField(
            model_name='event',
            name='manager',
        ),
    ]

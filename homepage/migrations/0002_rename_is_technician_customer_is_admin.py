# Generated by Django 4.1.3 on 2022-11-02 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='is_technician',
            new_name='is_admin',
        ),
    ]

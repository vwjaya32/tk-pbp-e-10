# Generated by Django 4.1 on 2022-10-31 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mh_tests', '0004_alter_mentaltest_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentaltest',
            name='date',
            field=models.DateTimeField(),
        ),
    ]

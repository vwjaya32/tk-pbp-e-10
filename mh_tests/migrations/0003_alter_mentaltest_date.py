# Generated by Django 4.1 on 2022-10-31 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mh_tests', '0002_mentaltest_date_mentaltest_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentaltest',
            name='date',
            field=models.DateField(),
        ),
    ]

# Generated by Django 4.1 on 2022-11-02 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_replies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replies',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

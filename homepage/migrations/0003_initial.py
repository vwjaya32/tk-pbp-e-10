# Generated by Django 4.1 on 2022-12-15 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0002_remove_customer_user_delete_address_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('kota', models.CharField(max_length=200)),
                ('kecamatan', models.CharField(max_length=200)),
                ('kelurahan', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.customer')),
            ],
        ),
    ]

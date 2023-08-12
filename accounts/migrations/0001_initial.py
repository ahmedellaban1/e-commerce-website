# Generated by Django 4.2.4 on 2023-08-12 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('code', models.CharField(blank=True, default='', max_length=6, null=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
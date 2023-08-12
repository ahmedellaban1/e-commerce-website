# Generated by Django 4.2.4 on 2023-08-12 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=120)),
                ('ZIP_code', models.CharField(max_length=5)),
                ('card_number', models.IntegerField()),
                ('card_expiry', models.DateField()),
                ('card_CVC', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('date', models.DateField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('repetition', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('status', models.CharField(max_length=15)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderBilling',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('billing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_info.billing')),
                ('oreder_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_info.order')),
            ],
        ),
    ]
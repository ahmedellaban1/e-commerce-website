# Generated by Django 4.2.4 on 2023-08-15 11:47

import django.core.validators
from django.db import migrations, models
import rules.file_uploader


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='', upload_to=rules.file_uploader.wrapper),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=23, validators=[django.core.validators.RegexValidator(code='ivalid_hexa_number', message='This field must contain at least one color and at most 3 colors in hexa format #XXXXXX', regex='^(#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})(,|$))+')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=1000, validators=[django.core.validators.RegexValidator(code='invalid_description', message='product description should be at least 20 characters and at most 1000 characters', regex='^.{20,1000}$')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=rules.file_uploader.wrapper),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default='S', max_length=3),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(max_length=200, validators=[django.core.validators.RegexValidator(code='invalid_review', message='review should be at least 20 characters and at most 200 characters', regex='^.{20,200}$')]),
        ),
    ]

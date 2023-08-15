# Generated by Django 4.2.4 on 2023-08-15 16:01

from django.db import migrations, models
import rules.file_uploader


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_product_size_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=rules.file_uploader.wrapper),
        ),
    ]
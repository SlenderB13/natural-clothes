# Generated by Django 4.0.6 on 2022-08-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
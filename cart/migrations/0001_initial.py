# Generated by Django 4.0.6 on 2022-07-29 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=9)),
                ('products', models.ManyToManyField(blank=True, to='core.product')),
            ],
        ),
    ]
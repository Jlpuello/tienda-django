# Generated by Django 3.0.3 on 2020-06-17 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_image'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(through='carts.CartProducts', to='products.Products'),
        ),
    ]
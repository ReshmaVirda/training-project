# Generated by Django 4.0 on 2022-01-31 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_alter_cart_pro_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productprice',
            field=models.IntegerField(default=0),
        ),
    ]

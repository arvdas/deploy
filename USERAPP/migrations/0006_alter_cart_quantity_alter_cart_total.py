# Generated by Django 4.2.4 on 2023-09-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERAPP', '0005_alter_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(),
        ),
    ]

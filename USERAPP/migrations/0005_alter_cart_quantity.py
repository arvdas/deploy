# Generated by Django 4.2.4 on 2023-09-20 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERAPP', '0004_alter_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
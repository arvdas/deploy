# Generated by Django 4.2.5 on 2023-09-25 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('USERAPP', '0007_remove_booking_phone_no_remove_booking_username_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='USERAPP.booking')),
            ],
        ),
    ]

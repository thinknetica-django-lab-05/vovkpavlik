# Generated by Django 3.2.8 on 2021-12-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_seller_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.CharField(blank=True, help_text='Номер телефона пользователя', max_length=12),
        ),
    ]
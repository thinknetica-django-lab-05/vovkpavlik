# Generated by Django 3.2.8 on 2021-12-15 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_alter_seller_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smslog',
            name='code',
            field=models.CharField(max_length=4),
        ),
    ]

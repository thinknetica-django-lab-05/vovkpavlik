# Generated by Django 3.2.8 on 2021-10-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211024_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

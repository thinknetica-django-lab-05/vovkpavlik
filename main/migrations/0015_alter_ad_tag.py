# Generated by Django 3.2.8 on 2021-11-11 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_ad_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='tag',
            field=models.ManyToManyField(to='main.Tag', verbose_name='Тэги'),
        ),
    ]

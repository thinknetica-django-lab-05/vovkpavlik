# Generated by Django 3.2.8 on 2021-11-13 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_adpicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adpicture',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ad', verbose_name='Объявление'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-11 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_ad_is_archive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.seller', verbose_name='Продавец'),
        ),
    ]
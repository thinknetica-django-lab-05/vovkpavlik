# Generated by Django 3.2.8 on 2021-12-15 14:59

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_alter_smslog_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smslog',
            name='code',
            field=models.CharField(default=main.models.get_random_code, max_length=4),
        ),
    ]

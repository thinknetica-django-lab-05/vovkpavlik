# Generated by Django 3.2.8 on 2022-02-05 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0055_alter_adpicture_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adpicture',
            name='test_field',
        ),
    ]

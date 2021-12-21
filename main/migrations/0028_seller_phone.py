# Generated by Django 3.2.8 on 2021-12-14 16:29

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_adpicture_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text="user's phone number", max_length=31),
        ),
    ]

# Generated by Django 3.2.8 on 2022-02-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_adpicture_test_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adpicture',
            name='image',
            field=models.ImageField(blank=True, default='images/ads/default-product.jpg', null=True, upload_to='images/ads/'),
        ),
    ]

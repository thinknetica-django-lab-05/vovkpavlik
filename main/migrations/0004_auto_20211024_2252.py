# Generated by Django 3.2.8 on 2021-10-24 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='ad',
            old_name='link',
            new_name='tag',
        ),
    ]

# Generated by Django 4.0.2 on 2023-08-16 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0002_rename_title_products_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]

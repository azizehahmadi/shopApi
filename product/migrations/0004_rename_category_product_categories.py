# Generated by Django 4.2.3 on 2023-07-05 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='categories',
        ),
    ]

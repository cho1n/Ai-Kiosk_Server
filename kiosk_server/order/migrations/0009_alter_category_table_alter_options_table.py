# Generated by Django 5.0.6 on 2024-06-03 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_rename_createdat_category_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='Category',
        ),
        migrations.AlterModelTable(
            name='options',
            table='Options',
        ),
    ]
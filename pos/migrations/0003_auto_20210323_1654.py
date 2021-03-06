# Generated by Django 3.1.7 on 2021-03-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0002_auto_20210315_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='creation_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_change_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order_item',
            name='creation_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order_item',
            name='last_change_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='creation_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_change_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

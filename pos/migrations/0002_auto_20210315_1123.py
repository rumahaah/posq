# Generated by Django 3.1.7 on 2021-03-15 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(default='customer 1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_item',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

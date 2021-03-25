# Generated by Django 3.1.7 on 2021-03-24 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0006_auto_20210323_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sequenceo',
            name='last',
        ),
        migrations.AddField(
            model_name='sequenceo',
            name='number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(blank=True, default='JD-03241', max_length=7),
        ),
        migrations.AlterField(
            model_name='sequenceo',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
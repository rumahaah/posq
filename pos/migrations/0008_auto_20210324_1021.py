# Generated by Django 3.1.7 on 2021-03-24 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0007_auto_20210324_1015'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SequenceO',
            new_name='Sequence',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(blank=True, default='JD-00000000', max_length=12),
        ),
    ]

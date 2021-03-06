# Generated by Django 3.2.3 on 2021-05-23 12:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earrings', '0008_alter_earring_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earring',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name=django.core.validators.MinValueValidator(0.01)),
        ),
        migrations.AlterField(
            model_name='earring',
            name='stock',
            field=models.IntegerField(verbose_name=django.core.validators.MinValueValidator(0)),
        ),
    ]

# Generated by Django 3.2 on 2021-05-09 09:07

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('earrings', '0004_auto_20210509_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='earring',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]

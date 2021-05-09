# Generated by Django 3.2 on 2021-05-09 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='collections',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.collections'),
            preserve_default=False,
        ),
    ]

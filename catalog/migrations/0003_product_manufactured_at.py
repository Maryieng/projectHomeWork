# Generated by Django 5.0.2 on 2024-02-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_product_manufactured_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateField(default='2020-10-16', verbose_name='Дата производства продукта'),
            preserve_default=False,
        ),
    ]

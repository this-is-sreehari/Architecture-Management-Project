# Generated by Django 4.1.7 on 2023-06-13 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_cart_delete_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
# Generated by Django 4.1.7 on 2023-07-27 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_cart_price_alter_cart_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mob', models.CharField(max_length=10)),
                ('mail', models.EmailField(max_length=254)),
                ('add1', models.CharField(max_length=30)),
                ('add2', models.CharField(max_length=30)),
                ('pin', models.CharField(max_length=6)),
                ('payment', models.CharField(choices=[('cod', 'Cash On Delivery'), ('upi', 'UPI'), ('nb', 'Net Banking')], default='cod', max_length=30)),
            ],
        ),
    ]
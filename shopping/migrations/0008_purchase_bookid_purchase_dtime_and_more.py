# Generated by Django 4.1.7 on 2023-07-27 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0007_purchase_amnt'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='bookid',
            field=models.CharField(default=django.utils.timezone.now, editable=False, max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='dtime',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='payment',
            field=models.CharField(choices=[('cod', 'Cash On Delivery'), ('upi', 'UPI'), ('nb', 'Net Banking')], max_length=30),
        ),
    ]

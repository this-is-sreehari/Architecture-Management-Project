# Generated by Django 4.1.7 on 2023-07-27 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='amnt',
            field=models.CharField(default=django.utils.timezone.now, max_length=6),
            preserve_default=False,
        ),
    ]

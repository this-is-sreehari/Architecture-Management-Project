# Generated by Django 4.1.7 on 2023-07-05 14:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0013_remove_requirements_water_requirements_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='cprofile',
            name='cl_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
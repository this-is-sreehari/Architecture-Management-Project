# Generated by Django 4.1.7 on 2023-07-28 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0014_cprofile_cl_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirements',
            name='requirement',
            field=models.TextField(max_length=300),
        ),
    ]

# Generated by Django 3.0.1 on 2021-03-10 21:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210310_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None),
        ),
    ]

# Generated by Django 3.0.1 on 2021-03-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.CharField(max_length=150, null=True),
        ),
    ]

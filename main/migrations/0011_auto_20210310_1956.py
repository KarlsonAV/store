# Generated by Django 3.0.1 on 2021-03-10 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
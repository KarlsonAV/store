# Generated by Django 3.0.1 on 2021-03-10 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(default=list, related_name='categories', to='main.Categories'),
        ),
    ]

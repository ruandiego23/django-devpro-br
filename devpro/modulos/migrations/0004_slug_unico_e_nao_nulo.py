# Generated by Django 5.0.6 on 2024-06-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0003_popular_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(max_length=125, unique=True),
        ),
    ]

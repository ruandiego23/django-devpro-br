# Generated by Django 5.0.6 on 2024-06-24 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0006_aula_iframe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='iframe_id',
            field=models.CharField(max_length=50),
        ),
    ]

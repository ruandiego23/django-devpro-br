# Generated by Django 5.0.6 on 2024-06-24 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='iframe_id',
            field=models.CharField(default=1, max_length=50),
        ),
    ]

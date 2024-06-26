# Generated by Django 5.0.6 on 2024-06-24 20:05

from django.db import migrations
from django.utils.text import slugify


def populate_slug(apps, schema_editor):
    Modulo = apps.get_model('modulos', 'Modulo')
    for modulo in Modulo.objects.all():
        modulo.slug = slugify(modulo.titulo)
        modulo.save()


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_modulo_slug'),
    ]

    operations = [
        migrations.RunPython(populate_slug),
    ]

# Generated by Django 5.0.6 on 2024-06-26 04:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0001_turma'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_de_inscricao', models.DateTimeField(auto_now_add=True)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turmas.turma')),
                ('usuario', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Matricula',
                'verbose_name_plural': 'Matriculas',
            },
        ),
        migrations.AddField(
            model_name='turma',
            name='estudantes',
            field=models.ManyToManyField(through='turmas.Matricula', to=settings.AUTH_USER_MODEL),
        ),
    ]

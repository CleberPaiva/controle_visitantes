# Generated by Django 4.2.4 on 2023-12-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nome_empresa',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nome da Empresa'),
        ),
    ]

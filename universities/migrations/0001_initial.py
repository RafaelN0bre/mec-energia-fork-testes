# Generated by Django 4.1 on 2022-10-06 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome da universidade por extenso', max_length=50, unique=True, verbose_name='Nome')),
                ('cnpj', models.CharField(help_text='14 números sem caracteres especiais', max_length=14, unique=True, verbose_name='CNPJ')),
            ],
        ),
    ]

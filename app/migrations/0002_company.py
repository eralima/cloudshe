# Generated by Django 3.2.7 on 2021-09-22 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('rua', models.CharField(max_length=150)),
                ('cep', models.CharField(max_length=150)),
                ('bairro', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=150)),
                ('fone', models.CharField(max_length=150)),
                ('cnpj', models.CharField(max_length=150)),
            ],
        ),
    ]

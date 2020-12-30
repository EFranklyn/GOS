# Generated by Django 3.1.4 on 2020-12-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OsCabecalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.CharField(max_length=20)),
                ('referencia', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=15)),
                ('logradouro', models.CharField(max_length=70)),
                ('complemento', models.CharField(max_length=70)),
                ('bairro', models.CharField(max_length=40)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=3)),
            ],
        ),
    ]
# Generated by Django 3.1.4 on 2020-12-23 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gos', '0002_auto_20201223_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='oscabecalho',
            name='dtpedido',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

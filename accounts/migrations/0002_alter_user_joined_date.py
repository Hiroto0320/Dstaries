# Generated by Django 4.0.1 on 2022-02-12 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joined_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 12, 16, 49, 3, 842941)),
        ),
    ]

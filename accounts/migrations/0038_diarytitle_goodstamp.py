# Generated by Django 4.0.2 on 2022-02-27 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_rename_country_user_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='diarytitle',
            name='goodstamp',
            field=models.IntegerField(default=0),
        ),
    ]

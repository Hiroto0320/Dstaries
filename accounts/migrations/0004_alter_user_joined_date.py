# Generated by Django 4.0.1 on 2022-02-12 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_joined_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joined_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

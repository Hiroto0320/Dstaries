# Generated by Django 4.0.2 on 2022-03-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_alter_user_dream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dream',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]

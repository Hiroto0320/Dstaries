# Generated by Django 4.0.2 on 2022-03-09 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_alter_user_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='diarycontent',
            name='image',
            field=models.ImageField(null=True, upload_to='content_image/'),
        ),
    ]

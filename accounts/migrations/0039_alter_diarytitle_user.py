# Generated by Django 4.0.2 on 2022-03-01 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_diarytitle_goodstamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarytitle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_diary_title', to=settings.AUTH_USER_MODEL),
        ),
    ]

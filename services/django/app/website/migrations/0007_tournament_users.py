# Generated by Django 5.0.7 on 2024-07-19 07:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20240715_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

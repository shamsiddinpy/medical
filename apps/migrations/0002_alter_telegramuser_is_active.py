# Generated by Django 5.1.5 on 2025-02-01 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Faolligi'),
        ),
    ]

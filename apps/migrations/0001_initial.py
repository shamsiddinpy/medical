# Generated by Django 5.1.5 on 2025-02-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255, unique=True, verbose_name='Foydalanuvchi ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='Telegram username')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Foydalanuvchi ismi')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Foydalanuvchi familiyasi')),
                ('language_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Til kodi (en, ru, uz, va hokazo)')),
                ('is_active', models.BooleanField(default=True, verbose_name='Faolligi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatga olingan vaqt")),
            ],
            options={
                'verbose_name': 'Telegram foydalanuvchisi',
                'verbose_name_plural': 'Telegram foydalanuvchilari',
            },
        ),
    ]

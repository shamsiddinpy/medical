from django.db import models


# Create your models here.


class TelegramUser(models.Model):
    user_id = models.CharField(max_length=255, unique=True, verbose_name="Foydalanuvchi ID")
    username = models.CharField(max_length=255, blank=True, null=True, verbose_name="Telegram username")
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Foydalanuvchi ismi")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Foydalanuvchi familiyasi")
    language_code = models.CharField(max_length=10, blank=True, null=True,
                                     verbose_name="Til kodi (en, ru, uz, va hokazo)")
    is_active = models.BooleanField(default=False, verbose_name="Faolligi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatga olingan vaqt")

    def __str__(self):
        return f"{self.first_name} {self.last_name} (@{self.username})"

    class Meta:
        verbose_name = "Telegram foydalanuvchisi"
        verbose_name_plural = "Telegram foydalanuvchilari"

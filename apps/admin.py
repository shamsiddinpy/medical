from django.contrib import admin

from apps.models import TelegramUser


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'first_name', 'last_name', 'language_code', 'is_active', 'created_at')
    search_fields = ('user_id', 'username', 'first_name', 'last_name')
    list_filter = ('is_active', 'language_code')

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model

from apps.models import TelegramUser

start_main_router = Router()
User = get_user_model()


@start_main_router.message(CommandStart())
async def start_main(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    language_code = message.from_user.language_code

    async def create_or_get_user():
        user_exist = await sync_to_async(TelegramUser.objects.filter(user_id=user_id).exists)()
        if not user_exist:
            await sync_to_async(TelegramUser.objects.create)(
                user_id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                language_code=language_code,
            )
            return None  # Return None if user was created
        else:
            return await sync_to_async(TelegramUser.objects.get)(user_id=user_id)

    user = await create_or_get_user()
    if user is None:
        await message.answer(f"Xush kelibsiz, {first_name}! Botdan foydalanishni boshlang.")
    else:
        if not user.is_active:
            await message.answer("Sizning hisobingiz bloklangan.")
        else:
            await message.answer(f"Xush kelibsiz, {first_name}! Botdan foydalanishni boshlang.")

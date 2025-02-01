from aiogram import Router

from apps.bot.handler.private.start_main import start_main_router

private_handler_router =  Router()

private_handler_router.include_routers(
start_main_router
)
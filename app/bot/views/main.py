from aiogram import Router, F
from aiogram.types import Message


router = Router()


@router.message(F.text)
async def echo_router(message: Message):
    await message.reply(text=message.text)

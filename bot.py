from aiogram import Bot, types
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor
from dotenv import load_dotenv
load_dotenv()


import os

token = token=os.getenv('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler() # Сюда попадаю сообщения
async def echo_send(message : types.Message):
    if message.text == "привет":
        await message.answer("И тебе привет")
    # await message.answer(message.text) # просто отвечает
    # await message.reply (message.text) # комментирует входящее сообщение
    await bot.send_message(message.from_user.id, message.text)# отправляет в личку, если написал уже

executor.start_polling(dp, skip_updates=True) # когда бот не онлайн не отвечает на прошлые сообщеения

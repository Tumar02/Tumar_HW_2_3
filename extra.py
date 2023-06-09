from aiogram import types, Dispatcher
from config import dp, bot


async def echo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=message.text)


async def words(message: types.Message):
    bad_words = ['shit', 'fuck', 'bull', 'bitch']
    for word in bad_words:
        if word in message.text.lower():
            await message.answer('quiet')


def register_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
    dp.register_message_handler(words)
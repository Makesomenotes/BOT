import asyncio
import logging
import time

import environs
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData

from kinopoisk_api import main

env = environs.Env()
env.read_env(".env")

bot = Bot(token=env.str('BOT_TOKEN'))

dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


callback_numbers = CallbackData("num", "action")


def get_keyboard_one(url):
    """ Кнопка на внешний ресурс """

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Ссылка", url=url))
    return keyboard


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """ Обработка команд start и help"""

    user_name = message.from_user.first_name
    if message.text == '/start':
        await message.answer(
            f"{user_name}, добрый день.\n"
            f"Я помогу вам найти фильм по его названию.\n"
            f"Отправьте мне название фильма.")
    elif message.text == '/help':
        await message.answer(
            f"Этот бот помогает найти фильм по его названию.\n"
            f" - Отправьте ему название фильма.\n"
            f" - Бот пришлет вам ссылку и краткую информацию о фильме.\n"
            f"Приятного просмотра!")


@dp.message_handler()
async def search(message: types.Message):
    """ Поиск по полученному названию"""

    search = await main(message.text)

    if "/" in message.text:
        await message.reply(
            "К сожалению, такой команды или фильма не найдено."
            "Попробуйте проверить правильность написания названия фильма или команды.")
    else:
        if search:
            for item in search:
                caption = f'{item.ru_name}\n\n' \
                          f'Год производства: {item.year}\n' \
                          f'Жанр: {", ".join(item.genres)}\n' \
                          f'Страна: {", ".join(item.countries)}\n' \
                          f'Время просмотра: {item.duration}\n' \
                          f'Рейтинг: {item.kp_rate}'

                await bot.send_photo(message.from_user.id, item.poster,
                                     caption=caption,
                                     reply_markup=get_keyboard_one(item.kp_url))
                time.sleep(0.5)
        else:
            await message.reply(
                "По вашему запросу ничего не смог найти,"
                " пожалуйста введите корректное название фильма.")


if __name__ == '__main__':
    executor.start_polling(dp)

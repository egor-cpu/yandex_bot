import yadisk
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from aiogram import types
from aiogram.filters import Command
import os
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv("passwords.env")
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
from create_report import *
from download_report import *
from edit_report import *
from update_temple import *

button_edit_report = KeyboardButton(text="Изменить Отчёт")
button_download_report = KeyboardButton(text="Выгрузить отчёт")
button_create_report = KeyboardButton(text="Создать отчёт")
button_update_temple = KeyboardButton(text="Обновить шаблоны")
button_registration = KeyboardButton(text="Зарегистрироваться")

greet_kb = ReplyKeyboardMarkup(keyboard=[[button_edit_report], [button_download_report], [button_create_report], [button_update_temple]], resize_keyboard=True)

@dp.message(Command(commands=["start"]))
async def start_command_handler(message: types.Message):
    await message.answer("Привет!", reply_markup=greet_kb)

if __name__ == '__main__':
    dp.run_polling(bot)
"""y = yadisk.YaDisk(token="y0_AgAAAABWsXjrAAySrgAAAAETpT3RAAB4d_H72nRPeo_nVzmz1CDWFma67w")
# или
# y = yadisk.YaDisk("<id-приложения>", "<secret-приложения>", "<токен>")

# Проверяет, валиден ли токен
print(y.check_token())

# Получает общую информацию о диске
print(y.get_disk_info())

# Выводит содержимое "/some/path"
print(list(y.listdir("/some/path")))

# Загружает "file_to_upload.txt" в "/destination.txt"
y.upload("file_to_upload.txt", "/destination.txt")

# То же самое
with open("file_to_upload.txt", "rb") as f:
    y.upload(f, "/destination.txt")

# Скачивает "/some-file-to-download.txt" в "downloaded.txt"
y.download("/some-file-to-download.txt", "downloaded.txt")

# Безвозвратно удаляет "/file-to-remove"
y.remove("/file-to-remove", permanently=True)

# Создаёт новую папку "/test-dir"
print(y.mkdir("/test-dir"))"""
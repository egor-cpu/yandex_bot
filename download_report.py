from main import dp, bot
import yadisk
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from aiogram import types
from aiogram.filters import Command
import os
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

@dp.message(lambda message: message.text == "Выгрузить отчёт")
async def exit_button_handler(message: types.Message):
    files = os.listdir("Отчёты")
    await message.answer("Выберите отчёт")
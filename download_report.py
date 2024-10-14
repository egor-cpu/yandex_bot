from main import dp, bot
import yadisk
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from aiogram import types
from aiogram.filters import Command
import os
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types.input_file import FSInputFile
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
lengh = 0
class sendStates(StatesGroup):
    waiting_for_message1 = State()
@dp.message(lambda message: message.text == "Выгрузить отчёт")
async def exit_button_handler(message: types.Message, state: FSMContext):
    files = os.listdir("Отчёты")
    global lengh
    a = len(files)
    print(a)
    lengh = a
    print(lengh)
    await message.answer("Выберите отчёт\n")
    for i in range(a):
        await message.answer(str(i+1)+". " + str(files[i]))

    await state.set_state(sendStates.waiting_for_message1)

@dp.message(sendStates.waiting_for_message1)
async def message_get1(message: types.Message, state: FSMContext):
    folder_path = 'Отчёты'
    files = os.listdir("Отчёты")
    for i in range(lengh):
        if message.text in files[i]:
            file_name = message.text
        elif message.text == i+1:
            file_name = files[i]
    try:
        for file_name in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, file_name)):
                file = FSInputFile(os.path.join(folder_path, file_name))
    except FileNotFoundError:
        await message.answer(f"Ошибка: папка {folder_path} не найдена.")
        return
    await message.answer_document(document=file)
    await state.clear()
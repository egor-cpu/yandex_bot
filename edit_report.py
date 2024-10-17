import openpyxl
from main import dp, bot
import yadisk
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from aiogram import types
from aiogram.filters import Command
import os
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
class editStates(StatesGroup):
    waiting_for_chose_document = State()
    waiting_for_worktype = State()
    waiting_for_chose_row = State()
    waiting_for_edit_row = State()
    waiting_for_chose_date = State()
    waiting_for_chose_category = State()
    waiting_for_chose_expense_item = State()
    waiting_for_chose_name = State()
    waiting_for_type = State()
    waiting_for_chose_count = State()
    waiting_for_chose_price = State()
    waiting_for_document_types = State()
    waiting_for_document = State()
    waiting_for_comments = State()
    waiting_for_accept_row = State()

filenamesave = ""
@dp.message(lambda message: message.text == "Изменить отчёт")
async def exel_edit(message: types.Message, state: FSMContext):
    files = os.listdir("Отчёты")
    global lengh
    a = len(files)
    print(a)
    lengh = a
    print(lengh)
    await message.answer("Выберите отчёт\n")
    for i in range(a):
        await message.answer(str(i + 1) + ". " + str(files[i]))
    await state.set_state(editStates.waiting_for_chose_document)

@dp.message(editStates.waiting_for_chose_document)
async def chose_document_get(message: types.Message, state: FSMContext):
    folder_path = 'Отчёты'
    files = os.listdir("Отчёты")
    global filenamesave
    file_name = message.text
    for i in range(lengh):
        if message.text in files[i]:
            file_name = message.text
        elif message.text == str(i+1):
            file_name = files[i]
    if os.path.exists(folder_path + "/" + file_name):
        filenamesave = file_name
        await message.answer("Выберите режим работы: \n 1. Изменить строку в отчёте \n 2. Добавить строку ")
        await state.set_state(editStates.waiting_for_worktype)
    else:
        await message.answer("Ошибка файла с " + message.text + " номером/названием не существует, проверьте правильность номера/названия введёного вами")

@dp.message(editStates.waiting_for_worktype)
async def worktype_get(message: types.Message, state: FSMContext):
    if message.text in "Изменить строку в отчёте" or message.text == str(1):
        await state.set_state(editStates.waiting_for_chose_row)
    elif message.text in "Добавить строку" or message.text == str(2):
        await message.answer("Введите дату покупки")
        await state.set_state(editStates.waiting_for_chose_date)
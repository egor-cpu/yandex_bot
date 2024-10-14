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
    waiting_for_chose = State()
    waiting_for_chose_row = State()
    waiting_for_edit_row = State()
    waiting_for_accept_row = State()
    waiting_for_chose_date = State()
    waiting_for_chose_category = State()
    waiting_for_chose_expense_item = State()
    waiting_for_chose_name = State()
    waiting_for_chose_count = State()
    waiting_for_chose_price = State()
    waiting_for_document = State()
    waiting_for_document_types = State()
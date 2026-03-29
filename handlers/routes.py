from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import FSInputFile
from keyboards import start_keyboard, next_question_keyboard
from aiogram.fsm.state import StatesGroup, State
import asyncio
import json
import random

router = Router()

class Form(StatesGroup):
    user_answer = State()
    question = State()

with open("dates.json", "r", encoding="utf-8") as f:
    dates = json.load(f)

async def ask_question(message: Message, state: FSMContext):
    question = random.choice(dates)

    allowed_themes = ["Давня доба", "Київська Русь", "Галицько-Волинська держава", "Литовсько-польська доба"]
    while not question["category"] in allowed_themes:
        question = random.choice(dates)

    await message.answer(f"{question["question"]}\n"
                         f"Формат відповіді: {question["format"]}")
    await state.update_data(question=question)
    await state.set_state(Form.user_answer)


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Цей бот допоможе вивчити дати з історії", reply_markup=start_keyboard())


@router.callback_query(lambda c: c.data == "learn_dates")
async def learn_dates(callback: CallbackQuery, state: FSMContext):
    await ask_question(callback.message, state)
    await callback.answer()


@router.message(Form.user_answer)
async def process_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    user_answer = message.text
    correct_answer = data.get("question")["answer"]

    if user_answer == correct_answer:
        await message.answer("✅Правильно", reply_markup=next_question_keyboard())

    else:
        await message.answer("❌Неправильно\n"
                             f"Правильна відповідь: {correct_answer}", reply_markup=next_question_keyboard())

    await state.clear()

    #await asyncio.sleep(1)
    #await ask_question(message)



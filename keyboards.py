from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📝Вчити дати", callback_data="learn_dates")],
            [InlineKeyboardButton(text="❓FAQ", callback_data="faq")]
        ]
    )
    return keyboard

def next_question_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➡️Наступне питання", callback_data="learn_dates")]
        ]
    )

    return keyboard
from aiogram import Bot, Dispatcher

from app.config import get_bot_token
from app.data_loader import load_questions
from app.handlers import create_router
from app.state import AppState


async def run_bot() -> None:
    questions, categories = load_questions("dates.json")
    if not questions:
        raise RuntimeError("Файл dates.json не містить питань.")

    state = AppState(questions=questions, categories=categories)

    bot = Bot(token=get_bot_token())
    dp = Dispatcher()
    dp.include_router(create_router(state))
    await dp.start_polling(bot)

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import (
    CALLBACK_NEXT,
    CALLBACK_RESTART,
    CALLBACK_THEME_PREFIX,
    CALLBACK_THEMES_DONE,
    build_next_keyboard,
    build_themes_keyboard,
)
from app.services import rebuild_remaining_questions, reset_user_progress, send_next_question
from app.state import AppState
from app.utils import normalize_text


def create_router(state: AppState) -> Router:
    router = Router()

    @router.message(Command("start"))
    async def cmd_start(message: Message) -> None:
        if not message.from_user:
            return

        reset_user_progress(state, message.from_user.id)
        session = state.get_session(message.from_user.id)

        await message.answer(
            "Вітаю! Це бот для вивчення дат з історії України.\n"
            "Оберіть теми, які хочете вивчати, і натисніть «Готово».",
            reply_markup=build_themes_keyboard(state.categories, session.selected_categories),
        )

    @router.callback_query(F.data.startswith(CALLBACK_THEME_PREFIX))
    async def toggle_theme(callback: CallbackQuery) -> None:
        session = state.get_session(callback.from_user.id)
        category_index_raw = callback.data.replace(CALLBACK_THEME_PREFIX, "", 1)

        if not category_index_raw.isdigit():
            await callback.answer("Некоректний вибір теми.", show_alert=True)
            return

        category_index = int(category_index_raw)
        if category_index < 0 or category_index >= len(state.categories):
            await callback.answer("Некоректний вибір теми.", show_alert=True)
            return

        category = state.categories[category_index]
        if category in session.selected_categories:
            session.selected_categories.remove(category)
        else:
            session.selected_categories.add(category)

        await callback.message.edit_reply_markup(
            reply_markup=build_themes_keyboard(state.categories, session.selected_categories)
        )
        await callback.answer()

    @router.callback_query(F.data == CALLBACK_THEMES_DONE)
    async def finish_theme_selection(callback: CallbackQuery) -> None:
        session = state.get_session(callback.from_user.id)

        if not session.selected_categories:
            await callback.answer("Оберіть хоча б одну тему.", show_alert=True)
            return

        rebuild_remaining_questions(state, callback.from_user.id)
        await callback.message.answer("Чудово! Починаємо тренування.")
        await send_next_question(callback, state, callback.from_user.id)
        await callback.answer()

    @router.message(F.text)
    async def check_answer(message: Message) -> None:
        if not message.from_user:
            return

        session = state.get_session(message.from_user.id)

        if not session.awaiting_answer or session.current_question_index is None:
            await message.answer("Щоб почати, введіть /start і оберіть теми для тренування.")
            return

        user_answer = normalize_text(message.text)
        question = state.questions[session.current_question_index]
        expected_answer = normalize_text(question.answer)

        session.awaiting_answer = False
        session.answered_count += 1

        if user_answer == expected_answer:
            await message.answer("✅ Правильно!", reply_markup=build_next_keyboard())
        else:
            await message.answer(
                "❌ Неправильно.\n"
                f"Правильна відповідь: {question.answer}",
                reply_markup=build_next_keyboard(),
            )

    @router.callback_query(F.data == CALLBACK_NEXT)
    async def next_question(callback: CallbackQuery) -> None:
        session = state.get_session(callback.from_user.id)
        if session.awaiting_answer:
            await callback.answer("Спочатку надішліть відповідь на поточне питання.")
            return

        await send_next_question(callback, state, callback.from_user.id)
        await callback.answer()

    @router.callback_query(F.data == CALLBACK_RESTART)
    async def restart_quiz(callback: CallbackQuery) -> None:
        session = state.get_session(callback.from_user.id)
        if not session.selected_categories:
            await callback.message.answer("Потрібно обрати теми заново. Введіть /start.")
            await callback.answer()
            return

        rebuild_remaining_questions(state, callback.from_user.id)
        await callback.message.answer("Новий раунд розпочато.")
        await send_next_question(callback, state, callback.from_user.id)
        await callback.answer()

    return router

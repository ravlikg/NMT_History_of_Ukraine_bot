import random

from aiogram.types import CallbackQuery, Message

from app.keyboards import build_restart_keyboard
from app.state import AppState


def reset_user_progress(state: AppState, user_id: int) -> None:
    session = state.get_session(user_id)
    session.selected_categories.clear()
    session.remaining_indices.clear()
    session.current_question_index = None
    session.awaiting_answer = False
    session.answered_count = 0


def rebuild_remaining_questions(state: AppState, user_id: int) -> None:
    session = state.get_session(user_id)
    session.remaining_indices = [
        idx for idx, q in enumerate(state.questions) if q.category in session.selected_categories
    ]
    random.shuffle(session.remaining_indices)
    session.current_question_index = None
    session.awaiting_answer = False
    session.answered_count = 0


async def send_next_question(
    target: Message | CallbackQuery, state: AppState, user_id: int
) -> None:
    session = state.get_session(user_id)
    if not session.remaining_indices:
        session.current_question_index = None
        session.awaiting_answer = False
        text = (
            "Ви пройшли всі питання з обраних тем.\n"
            f"Усього відповідей у цій сесії: {session.answered_count}\n\n"
            "Натисніть кнопку нижче, щоб почати знову."
        )
        if isinstance(target, Message):
            await target.answer(text, reply_markup=build_restart_keyboard())
        else:
            await target.message.answer(text, reply_markup=build_restart_keyboard())
        return

    question_index = session.remaining_indices.pop()
    session.current_question_index = question_index
    session.awaiting_answer = True
    question = state.questions[question_index]

    question_text = (
        f"Тема: {question.category}\n\n"
        f"Питання:\n{question.question}\n\n"
        f"Формат відповіді: {question.answer_format}"
    )

    if isinstance(target, Message):
        await target.answer(question_text)
    else:
        await target.message.answer(question_text)

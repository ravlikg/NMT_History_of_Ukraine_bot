from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

CALLBACK_THEME_PREFIX = "theme:"
CALLBACK_THEMES_DONE = "themes_done"
CALLBACK_NEXT = "next_question"
CALLBACK_RESTART = "restart_quiz"


def build_themes_keyboard(categories: list[str], selected: set[str]) -> InlineKeyboardMarkup:
    rows: list[list[InlineKeyboardButton]] = []
    for index, category in enumerate(categories):
        prefix = "✅" if category in selected else "☑️"
        rows.append(
            [
                InlineKeyboardButton(
                    text=f"{prefix} {category}",
                    callback_data=f"{CALLBACK_THEME_PREFIX}{index}",
                )
            ]
        )

    rows.append([InlineKeyboardButton(text="Готово", callback_data=CALLBACK_THEMES_DONE)])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def build_next_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Наступне питання", callback_data=CALLBACK_NEXT)]
        ]
    )


def build_restart_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Почати знову", callback_data=CALLBACK_RESTART)]]
    )

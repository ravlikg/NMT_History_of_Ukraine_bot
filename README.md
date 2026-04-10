# Telegram-бот для вивчення дат з історії України

Простий бот на `aiogram`, який:
- пропонує обрати теми;
- ставить випадкові питання з обраних тем;
- не повторює питання, доки не завершиться набір;
- перевіряє відповідь і показує правильний варіант у разі помилки;
- після відповіді показує кнопку `Наступне питання`;
- підказує формат відповіді (`рік`, `рік - рік`, `день місяць рік` тощо).

## Вимоги
- Python 3.10+
- Telegram Bot Token у файлі `.env`

## Налаштування
1. Встановіть залежності:
   ```bash
   pip install -r requirements.txt
   ```
2. Переконайтесь, що у `.env` є:
   ```env
   BOT_TOKEN=your_token_here
   ```
3. Переконайтесь, що `dates.json` знаходиться в корені проєкту.
4. Для нового запуску можна скопіювати шаблон:
   ```bash
   cp .env.example .env
   ```
   (у Windows PowerShell: `copy .env.example .env`)

## Запуск
```bash
python bot.py
```

## Структура проєкту
- `bot.py` — точка входу.
- `app/main.py` — ініціалізація бота та роутерів.
- `app/config.py` — завантаження конфігурації з `.env`.
- `app/data_loader.py` — читання `dates.json`.
- `app/models.py` — моделі даних і сесії.
- `app/state.py` — in-memory стан застосунку.
- `app/services.py` — бізнес-логіка квізу.
- `app/keyboards.py` — інлайн-клавіатури та callback-константи.
- `app/handlers.py` — Telegram-хендлери.
- `app/utils.py` — допоміжні функції (нормалізація тексту).

## Використання
1. Напишіть боту `/start`.
2. Оберіть потрібні теми.
3. Натисніть `Готово`.
4. Введіть відповідь у потрібному форматі.
5. Натисніть `Наступне питання`.

## Публікація на GitHub
1. Створіть порожній репозиторій на GitHub (без `README`, `.gitignore` та license).
2. Ініціалізуйте і закомітьте локально:
   ```bash
   git add .
   git commit -m "Initial commit: aiogram history quiz bot"
   ```
3. Прив'яжіть віддалений репозиторій та запуште:
   ```bash
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```

Важливо: файл `.env` уже додано в `.gitignore`, тому токен не потрапить у репозиторій.

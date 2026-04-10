# History Dates Telegram Bot (aiogram)

Telegram-бот для тренування дат з історії України.  
Бот повністю українською мовою та працює у форматі навчального квізу.

## Можливості

- вибір тем перед стартом тренування;
- випадкові питання тільки з обраних тем;
- без повторів, доки не буде пройдено весь набір;
- перевірка відповіді з показом правильного варіанта;
- кнопка `Наступне питання` після кожної відповіді;
- підказка формату відповіді (`рік`, `рік - рік`, `день місяць рік` тощо).

## Технології

- Python 3.10+
- [aiogram 3](https://docs.aiogram.dev/)
- `python-dotenv`

## Структура проєкту

```text
.
├─ app/
│  ├─ __init__.py
│  ├─ main.py          # ініціалізація бота
│  ├─ handlers.py      # Telegram handlers
│  ├─ services.py      # бізнес-логіка квізу
│  ├─ state.py         # in-memory стан користувачів
│  ├─ keyboards.py     # inline клавіатури
│  ├─ data_loader.py   # читання dates.json
│  ├─ models.py        # dataclasses моделей
│  ├─ config.py        # BOT_TOKEN з .env
│  └─ utils.py         # нормалізація тексту
├─ bot.py              # точка входу
├─ dates.json          # база питань
├─ requirements.txt
├─ .env.example
└─ .gitignore
```

## Быстрый старт

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Создайте файл окружения:
   - Linux/macOS:
     ```bash
     cp .env.example .env
     ```
   - Windows PowerShell:
     ```powershell
     copy .env.example .env
     ```
3. Вставьте токен в `.env`:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   ```
4. Убедитесь, что `dates.json` находится в корне проекта.
5. Запустите бота:
   ```bash
   python bot.py
   ```

## Использование

1. Отправьте боту `/start`.
2. Выберите темы.
3. Нажмите `Готово`.
4. Введите ответ в нужном формате.
5. Нажмите `Наступне питання`.

## Безопасность

- Файл `.env` игнорируется через `.gitignore`.
- Никогда не публикуйте реальный `BOT_TOKEN`.
- Если токен уже где-то засветился, перевыпустите его через BotFather.

# Expense Bot — Telegram-бот для учёта расходов

Telegram-бот, который помогает вести учёт личных расходов. Ты просто пишешь боту, сколько и на что потратил, а он сохраняет всё в базу данных и считает статистику.

## Что умеет

- **`/start`** — регистрация. Бот создаёт запись о тебе в базе.
- **`/add 500 еда`** — добавить трату. Сумма и категория.
- **`/list`** — показать все траты за всё время.
- **`/stats`** — статистика: сумма по каждой категории.
- **`/delete 5`** — удалить трату по ID.

## Стек технологий

| Технология | Зачем |
|------------|-------|
| Python 3.11 | Язык разработки |
| aiogram 3.x | Работа с Telegram Bot API |
| Postgres 16 | Хранение данных |
| psycopg2 | Подключение к Postgres из Python |
| Docker | Упаковка проекта в контейнер |
| Docker Compose | Запуск бота и базы одной командой |

## Структура проекта
expense-bot/
├── bot/
│ ├── init.py
│ ├── config.py # Загрузка переменных окружения
│ ├── db.py # Работа с Postgres
│ └── main.py # Логика бота
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .gitignore
└── README.md

text

## Как запустить

1. **Установи Docker Desktop.**

2. **Клонируй репозиторий:**
git clone https://github.com/LFG-Aizen/expense-bot.git
cd expense-bot

text

3. **Создай файл `.env`** в корне проекта:
BOT_TOKEN=твой_токен_от_BotFather
DB_HOST=db
DB_PORT=5432
DB_NAME=expenses
DB_USER=postgres
DB_PASSWORD=secret

text

4. **Запусти:**
docker compose up --build

text

5. **Открой Telegram, найди своего бота, напиши `/start`.**

## Как пользоваться

1. Напиши `/start` — бот зарегистрирует тебя.
2. Добавь трату: `/add 500 еда`.
3. Посмотри все траты: `/list`.
4. Посмотри статистику: `/stats`.
5. Удали лишнее: `/delete 5`.

## Что можно добавить позже

- Экспорт трат в CSV.
- Графики по категориям.
- Лимиты бюджета и уведомления.
- Веб-интерфейс для просмотра статистики.

## Скриншоты

1.png)
2.png)

## Автор

Aizen — [GitHub](https://github.com/LFG-Aizen)

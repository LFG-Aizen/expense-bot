import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from bot.config import BOT_TOKEN
from bot.db import (
    init_db, add_user, add_expense,
    get_expenses, get_stats, delete_expense,
)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    add_user(message.from_user.id)
    await message.answer(
        "Привет! Я бот для учёта расходов.\n\n"
        "Команды:\n"
        "/add 500 еда — добавить трату\n"
        "/list — все траты\n"
        "/stats — статистика\n"
        "/delete 5 — удалить трату по ID"
    )


@dp.message(Command("add"))
async def cmd_add(message: Message):
    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        await message.answer("Формат: /add 500 еда")
        return
    try:
        amount = int(parts[1])
    except ValueError:
        await message.answer("Сумма должна быть числом.")
        return
    category = parts[2]
    add_expense(message.from_user.id, amount, category)
    await message.answer(f"Добавлено: {amount} — {category}")


@dp.message(Command("list"))
async def cmd_list(message: Message):
    rows = get_expenses(message.from_user.id)
    if not rows:
        await message.answer("Трат пока нет.")
        return
    text = "\n".join(
        f"{r[0]}. {r[1]} — {r[2]} ({r[3].strftime('%d.%m.%Y')})" for r in rows
    )
    await message.answer(text)


@dp.message(Command("stats"))
async def cmd_stats(message: Message):
    rows = get_stats(message.from_user.id)
    if not rows:
        await message.answer("Статистики пока нет.")
        return
    text = "\n".join(f"{r[0]}: {r[1]}" for r in rows)
    await message.answer(text)


@dp.message(Command("delete"))
async def cmd_delete(message: Message):
    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("Формат: /delete 5")
        return
    try:
        expense_id = int(parts[1])
    except ValueError:
        await message.answer("ID должен быть числом.")
        return
    delete_expense(message.from_user.id, expense_id)
    await message.answer(f"Удалено: {expense_id}")


async def main():
    init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
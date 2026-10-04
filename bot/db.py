import psycopg2
from bot.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            telegram_id BIGINT UNIQUE NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id SERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL,
            amount INTEGER NOT NULL,
            category VARCHAR(50) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


def add_user(telegram_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (telegram_id) VALUES (%s) ON CONFLICT DO NOTHING;",
        (telegram_id,),
    )
    conn.commit()
    cur.close()
    conn.close()


def add_expense(telegram_id, amount, category):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO expenses (user_id, amount, category) VALUES (%s, %s, %s);",
        (telegram_id, amount, category),
    )
    conn.commit()
    cur.close()
    conn.close()


def get_expenses(telegram_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, amount, category, created_at FROM expenses WHERE user_id = %s ORDER BY created_at DESC;",
        (telegram_id,),
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def get_stats(telegram_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT category, SUM(amount) FROM expenses WHERE user_id = %s GROUP BY category;",
        (telegram_id,),
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def delete_expense(telegram_id, expense_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM expenses WHERE id = %s AND user_id = %s;",
        (expense_id, telegram_id),
    )
    conn.commit()
    cur.close()
    conn.close()
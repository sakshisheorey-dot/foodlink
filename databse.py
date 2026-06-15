import sqlite3


DB_NAME = "foodlink.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS donations(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        donor_id INTEGER,
        category TEXT,
        quantity INTEGER,
        description TEXT,
        expiry TEXT,
        location TEXT,
        image_path TEXT,
        status TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ngos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        cause TEXT,
        location TEXT,
        rating REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requests(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        donation_id INTEGER,
        ngo_id INTEGER,
        status TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rewards(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        points INTEGER
    )
    """)

    conn.commit()
    conn.close()


create_tables()
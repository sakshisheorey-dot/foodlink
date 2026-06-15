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

import pandas as pd


def add_donation(
    donor_id,
    category,
    quantity,
    description,
    expiry,
    location,
    image_path,
    status="Posted"
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO donations
        (
        donor_id,
        category,
        quantity,
        description,
        expiry,
        location,
        image_path,
        status
        )
        VALUES (?,?,?,?,?,?,?,?)
    """,
    (
        donor_id,
        category,
        quantity,
        description,
        expiry,
        location,
        image_path,
        status
    ))

    conn.commit()
    conn.close()


def get_all_donations():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM donations",
        conn
    )

    conn.close()

    return df


def create_request(
    donation_id,
    ngo_id,
    status="Pending"
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO requests
        (donation_id, ngo_id, status)
        VALUES (?,?,?)
    """,
    (
        donation_id,
        ngo_id,
        status
    ))

    conn.commit()
    conn.close()


def get_requests():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM requests",
        conn
    )

    conn.close()

    return df
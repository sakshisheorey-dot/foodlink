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
    cursor.execute("""
CREATE TABLE IF NOT EXISTS notifications(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS badges(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    badge_name TEXT
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

import pandas as pd


def get_donation_by_id(donation_id):

    conn = get_connection()

    df = pd.read_sql_query(
        f"""
        SELECT *
        FROM donations
        WHERE id={donation_id}
        """,
        conn
    )

    conn.close()

    return df


def update_donation_status(
    donation_id,
    status
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE donations
    SET status=?
    WHERE id=?
    """,
    (status, donation_id))

    conn.commit()
    conn.close()


def get_impact_metrics():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM donations",
        conn
    )

    conn.close()

    return df


def get_ngos():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM ngos",
        conn
    )

    conn.close()

    return df


def get_user_rewards(user_id):

    conn = get_connection()

    df = pd.read_sql_query(
        f"""
        SELECT *
        FROM rewards
        WHERE user_id={user_id}
        """,
        conn
    )

    conn.close()

    return df


def get_notifications(user_id):

    conn = get_connection()

    df = pd.read_sql_query(
        f"""
        SELECT *
        FROM notifications
        WHERE user_id={user_id}
        ORDER BY created_at DESC
        """,
        conn
    )

    conn.close()

    return df


def get_badges(user_id):

    conn = get_connection()

    df = pd.read_sql_query(
        f"""
        SELECT *
        FROM badges
        WHERE user_id={user_id}
        """,
        conn
    )

    conn.close()

    return df
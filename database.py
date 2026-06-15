import sqlite3
from datetime import datetime

DB_NAME = "foodlink.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT,
        points INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Food Posts
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS food_posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        donor_id INTEGER,
        food_type TEXT,
        quantity INTEGER,
        description TEXT,
        expiry_time TEXT,
        location TEXT,
        image_path TEXT,
        status TEXT DEFAULT 'Available',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # NGO Requests
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ngo_requests(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        food_id INTEGER,
        ngo_id INTEGER,
        status TEXT DEFAULT 'Pending',
        requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Tracking
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS donation_tracking(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        food_id INTEGER,
        current_stage TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Rewards
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS badges(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        badge_name TEXT,
        earned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


# --------------------------
# USER OPERATIONS
# --------------------------

def create_user(name, email, password, role):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users(name,email,password,role)
    VALUES(?,?,?,?)
    """, (name, email, password, role))

    conn.commit()
    conn.close()


def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()
    return user


def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id=?",
        (user_id,)
    )

    user = cursor.fetchone()

    conn.close()
    return user


# --------------------------
# FOOD OPERATIONS
# --------------------------

def create_food_post(
        donor_id,
        food_type,
        quantity,
        description,
        expiry_time,
        location,
        image_path):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO food_posts(
        donor_id,
        food_type,
        quantity,
        description,
        expiry_time,
        location,
        image_path
    )
    VALUES(?,?,?,?,?,?,?)
    """,
    (
        donor_id,
        food_type,
        quantity,
        description,
        expiry_time,
        location,
        image_path
    ))

    conn.commit()
    conn.close()


def get_all_food():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM food_posts
    ORDER BY created_at DESC
    """)

    data = cursor.fetchall()

    conn.close()
    return data


def get_available_food():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM food_posts
    WHERE status='Available'
    ORDER BY created_at DESC
    """)

    data = cursor.fetchall()

    conn.close()
    return data


def update_food_status(food_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE food_posts
    SET status=?
    WHERE id=?
    """, (status, food_id))

    conn.commit()
    conn.close()


# --------------------------
# REQUESTS
# --------------------------

def create_request(food_id, ngo_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO ngo_requests(food_id, ngo_id)
    VALUES(?,?)
    """, (food_id, ngo_id))

    conn.commit()
    conn.close()


def get_requests():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM ngo_requests
    ORDER BY requested_at DESC
    """)

    data = cursor.fetchall()

    conn.close()
    return data


# --------------------------
# TRACKING
# --------------------------

def update_tracking(food_id, stage):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO donation_tracking(
        food_id,
        current_stage
    )
    VALUES(?,?)
    """, (food_id, stage))

    conn.commit()
    conn.close()


def get_tracking(food_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM donation_tracking
    WHERE food_id=?
    """, (food_id,))

    data = cursor.fetchall()

    conn.close()
    return data

def update_request_status(request_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE ngo_requests
    SET status=?
    WHERE id=?
    """, (status, request_id))

    conn.commit()
    conn.close()


def get_food_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM food_posts"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count
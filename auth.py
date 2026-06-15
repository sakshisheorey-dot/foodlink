import sqlite3

DB_NAME = "foodlink.db"


def signup(name, email, password, role):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO users
        (name,email,password,role)
        VALUES (?,?,?,?)
        """, (name,email,password,role))

        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()


def login(email,password):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users
    WHERE email=? AND password=?
    """,(email,password))

    user = cursor.fetchone()

    conn.close()

    return user
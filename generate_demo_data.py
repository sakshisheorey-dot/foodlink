import sqlite3
import random

conn = sqlite3.connect(
    "foodlink.db"
)

cursor = conn.cursor()

categories = [
    "Cooked Food",
    "Vegetables",
    "Fruits",
    "Bakery"
]

for i in range(30):

    cursor.execute("""
    INSERT INTO donations(
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
        1,
        random.choice(categories),
        random.randint(5,50),
        "Fresh surplus food",
        "2026-06-20",
        "Hyderabad",
        "",
        "Posted"
    ))

conn.commit()
conn.close()
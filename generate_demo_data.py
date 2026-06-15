from faker import Faker
import sqlite3
import random

fake = Faker()

conn = sqlite3.connect("foodlink.db")
cursor = conn.cursor()

food_types = [
    "Cooked Food",
    "Vegetables",
    "Bakery",
    "Fruits",
    "Rice"
]

locations = [
    "Gachibowli",
    "Madhapur",
    "Kompally",
    "Secunderabad",
    "Begumpet"
]

for i in range(50):

    cursor.execute("""
    INSERT INTO food_posts(
        donor_id,
        food_type,
        quantity,
        description,
        expiry_time,
        location,
        status
    )
    VALUES(?,?,?,?,?,?,?)
    """,
    (
        1,
        random.choice(food_types),
        random.randint(10,100),
        fake.sentence(),
        "2026-12-31",
        random.choice(locations),
        random.choice(
            [
                "Available",
                "Claimed",
                "Delivered"
            ]
        )
    ))

conn.commit()
conn.close()

print("Demo Data Generated")
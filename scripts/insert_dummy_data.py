import sqlite3

import os
conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'marketing_ai.db')))

cursor = conn.cursor()

# 1️⃣ Dummy Customers
customers = [
    ("Alice", 28, "Female", 55000, "New York"),
    ("Bob", 35, "Male", 72000, "Los Angeles"),
    ("Charlie", 23, "Male", 48000, "Chicago"),
    ("Diana", 31, "Female", 63000, "Houston"),
    ("Eva", 42, "Female", 87000, "Seattle")
]

cursor.executemany("""
    INSERT INTO customers (name, age, gender, income, location)
    VALUES (?, ?, ?, ?, ?);
""", customers)

# 2️⃣ Dummy Offers
offers = [
    ("10% off Electronics", "Electronics", 10.0, "Get 10% off on all electronic items!"),
    ("Free Shipping", "Logistics", 0.0, "Enjoy free shipping on orders above $50."),
    ("Buy 1 Get 1 Free", "Apparel", 50.0, "Special BOGO offer on select apparels."),
    ("20% off for New Users", "General", 20.0, "Exclusive 20% discount for new users."),
    ("Loyalty Bonus", "Loyalty", 15.0, "You’ve earned a loyalty bonus! 15% off.")
]

cursor.executemany("""
    INSERT INTO offers (title, category, discount, message)
    VALUES (?, ?, ?, ?);
""", offers)

conn.commit()
conn.close()

print("✅ Dummy data inserted into customers and offers tables.")

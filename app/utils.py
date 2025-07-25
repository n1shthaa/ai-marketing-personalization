import sqlite3
import os
import pandas as pd

def connect_db():
    db_path = os.path.join("database", "marketing_ai.db")
    try:
        conn = sqlite3.connect(db_path, check_same_thread=False)
        return conn
    except Exception as e:
        print("❌ SQLite connection error:", e)
        return None
def fetch_customers(conn):
    query = "SELECT * FROM customers;"
    return pd.read_sql(query, conn)

def fetch_offers(conn):
    query = "SELECT * FROM offers;"
    return pd.read_sql(query, conn)
import sqlite3

def run_sql_file(db_path, sql_file_path):
    # Connect to SQLite DB
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Read SQL from file
    with open(sql_file_path, 'r') as file:
        sql_script = file.read()

    try:
        cursor.executescript(sql_script)
        conn.commit()
        print("✅ Schema created successfully in", db_path)
    except Exception as e:
        print("❌ Error creating schema:", e)
    finally:
        conn.close()

# Run the script
run_sql_file("database/marketing_ai.db", "database/init.sql")

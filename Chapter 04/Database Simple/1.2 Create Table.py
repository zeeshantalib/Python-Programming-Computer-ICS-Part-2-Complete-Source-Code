import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        rollno TEXT,
        class_name TEXT
    )
""")

connection.commit()
connection.close()

print("Table created!")
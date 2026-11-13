import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute(
    "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
    ("Ahmad", 15, "8th")
)

connection.commit()

print("Student inserted successfully!")

connection.close()
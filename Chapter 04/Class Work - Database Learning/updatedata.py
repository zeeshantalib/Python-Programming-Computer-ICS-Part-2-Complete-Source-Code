import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute(
    "UPDATE students SET age = ? WHERE id = ?",
    (10, 4)
)

connection.commit()

print("Student updated successfully!")

connection.close()
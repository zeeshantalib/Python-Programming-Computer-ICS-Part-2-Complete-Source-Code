import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

student_id = 10

cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (student_id,)
)

connection.commit()

print("Student deleted successfully!")

connection.close()
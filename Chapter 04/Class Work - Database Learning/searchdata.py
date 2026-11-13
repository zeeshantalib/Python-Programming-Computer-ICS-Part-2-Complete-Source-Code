import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

student_id = 1

cursor.execute(
    "SELECT * FROM students WHERE id = ?",
    (student_id,)
)

record = cursor.fetchone()

if record:
    print("Student Found:", record)
else:
    print("Student not found!")

connection.close()
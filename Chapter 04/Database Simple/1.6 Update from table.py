import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()
cursor.execute("""
    UPDATE students
    SET name = ?, rollno = ?, class_name = ?
    WHERE id = ?
""", ("Ali Khan", "CS005", "BSCS", 5))



cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

connection.close()
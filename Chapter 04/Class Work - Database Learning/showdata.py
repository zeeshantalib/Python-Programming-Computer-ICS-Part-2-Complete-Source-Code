import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

for row in records:
    print(row)

connection.close()
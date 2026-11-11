import sqlite3

connection = sqlite3.connect("students.db")

print("Database connected!")

connection.close()
# Import sqlite3 module
import sqlite3

# Connect to the database file named "school.db"
# If the file does not exist, SQLite will create it automatically
connection = sqlite3.connect("school.db")

# Create a cursor object
# Cursor is used to execute SQL queries
cursor = connection.cursor()

# Create "students" table if it does not exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        grade TEXT
    )
""")

# (Optional) Insert sample data
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Ali', 14, '8th')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Sara', 15, '9th')")

# Save changes
connection.commit()

# This query selects all columns (*) from the table named "students"
cursor.execute("SELECT * FROM students")

# Fetch all records returned by the query
# fetchall() returns a list of rows/records
records = cursor.fetchall()

# Display all records
# Loop through each row in the records list
for row in records:
    # Print each row of the table
    print(row)

# Close the database connection
connection.close()
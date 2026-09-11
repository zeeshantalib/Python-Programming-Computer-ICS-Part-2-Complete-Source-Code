import sqlite3

# Connect to the database
connection = sqlite3.connect("school.db")

# Create a cursor object
cursor = connection.cursor()

# Execute DELETE query (example: delete student with ID = 1)
cursor.execute("DELETE FROM students WHERE id = 1")

# Save changes
connection.commit()

# Display confirmation
print("Record deleted successfully")

# Close the connection
connection.close()
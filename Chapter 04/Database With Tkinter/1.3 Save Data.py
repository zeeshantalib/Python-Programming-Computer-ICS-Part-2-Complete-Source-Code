import tkinter as tk
import sqlite3


def save_student():

    name = name_entry.get()
    rollno = roll_entry.get()
    class_name = class_entry.get()

    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students (name, rollno, class_name)
        VALUES (?, ?, ?)
    """, (name, rollno, class_name))

    connection.commit()
    connection.close()

    print("Student saved!")


window = tk.Tk()

window.title("Student Management")
window.geometry("500x400")


tk.Label(window, text="Student Name").pack()

name_entry = tk.Entry(window)
name_entry.pack()


tk.Label(window, text="Roll Number").pack()

roll_entry = tk.Entry(window)
roll_entry.pack()


tk.Label(window, text="Class").pack()

class_entry = tk.Entry(window)
class_entry.pack()


tk.Button(
    window,
    text="Save Student",
    command=save_student
).pack()


window.mainloop()
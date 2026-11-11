import tkinter as tk
from tkinter import ttk
import sqlite3


def load_students():

    for row in tree.get_children():
        tree.delete(row)

    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    connection.close()

    for student in students:
        tree.insert("", tk.END, values=student)


window = tk.Tk()

window.title("Student Management")
window.geometry("700x400")


tree = ttk.Treeview(
    window,
    columns=("id", "name", "rollno", "class"),
    show="headings"
)

tree.heading("id", text="ID")
tree.heading("name", text="Name")
tree.heading("rollno", text="Roll No")
tree.heading("class", text="Class")

tree.pack(fill="both", expand=True)


tk.Button(
    window,
    text="Load Students",
    command=load_students
).pack()


window.mainloop()
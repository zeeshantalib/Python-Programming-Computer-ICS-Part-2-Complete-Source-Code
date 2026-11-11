import tkinter as tk

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

window.mainloop()
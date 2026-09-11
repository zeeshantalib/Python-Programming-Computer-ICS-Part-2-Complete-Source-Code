#student card
import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Student Information")
window.geometry("600x400")
window.configure(bg="white")


# Create frame
card = tk.Frame(
    window,
    bg="lightgray",
    padx=30,
    pady=20,
    bd=2,
    relief="solid"
)

# Title
title = tk.Label(
    card,
    text="Student Information",
    font=("Arial", 22, "bold"),
    bg="lightgray"
)

# Student information
name = tk.Label(
    card,
    text="Name: Ali Ahmed",
    font=("Arial", 14),
    bg="lightgray"
)

age = tk.Label(
    card,
    text="Age: 20",
    font=("Arial", 14),
    bg="lightgray"
)

course = tk.Label(
    card,
    text="Course: Python",
    font=("Arial", 14),
    bg="lightgray"
)

status = tk.Label(
    card,
    text="Status: Active",
    font=("Arial", 14, "bold"),
    fg="green",
    bg="lightgray"
)

# Display widgets
card.pack(pady=50)

title.pack(pady=10)
name.pack(pady=5)
age.pack(pady=5)
course.pack(pady=5)
status.pack(pady=5)

window.mainloop()
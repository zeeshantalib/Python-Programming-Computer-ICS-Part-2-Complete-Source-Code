import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Multiple Labels")
window.geometry("500x350")

# Create labels
title_label = tk.Label(
    window,
    text="Student Information",
    font=("Arial", 20, "bold")
)

name_label = tk.Label(
    window,
    text="Name: Ali"
)

age_label = tk.Label(
    window,
    text="Age: 20"
)

course_label = tk.Label(
    window,
    text="Course: Python"
)

# Display labels
title_label.pack(pady=20)
name_label.pack(pady=5)
age_label.pack(pady=5)
course_label.pack(pady=5)

window.mainloop()
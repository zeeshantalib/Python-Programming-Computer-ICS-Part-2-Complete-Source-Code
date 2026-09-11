import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Grid Span")
window.geometry("600x400")

# Heading
heading = tk.Label(
    window,
    text="Registration Form",
    font=("Arial", 20, "bold")
)

# Form widgets
name_label = tk.Label(window, text="Name:")
name_entry = tk.Entry(window, width=30)

email_label = tk.Label(window, text="Email:")
email_entry = tk.Entry(window, width=30)

button = tk.Button(
    window,
    text="Submit"
)

# Position widgets
heading.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=20
)

name_label.grid(row=1, column=0, padx=10, pady=10)
name_entry.grid(row=1, column=1, padx=10, pady=10)

email_label.grid(row=2, column=0, padx=10, pady=10)
email_entry.grid(row=2, column=1, padx=10, pady=10)

button.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=20
)

window.mainloop()
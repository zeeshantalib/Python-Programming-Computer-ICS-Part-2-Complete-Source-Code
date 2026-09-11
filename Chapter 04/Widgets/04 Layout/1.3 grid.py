import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Grid Layout")
window.geometry("600x350")

# Create widgets
tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(window, width=30).grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Email:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(window, width=30).grid(row=1, column=1, padx=10, pady=10)

tk.Button(window, text="Submit").grid(
    row=2,
    column=1,
    pady=20
)

window.mainloop()
import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Grid Properties")
window.geometry("600x350")

# Create widgets
label = tk.Label(window, text="Username:")
entry = tk.Entry(window, width=30)
button = tk.Button(window, text="Login")

# Position widgets
label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
button.grid(row=1, column=1, padx=10, pady=20)

window.mainloop()
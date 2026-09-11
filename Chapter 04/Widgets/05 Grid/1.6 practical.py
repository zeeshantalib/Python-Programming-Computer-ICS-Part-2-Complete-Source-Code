import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Registration Form")
window.geometry("600x450")

# Heading
tk.Label(
    window,
    text="Registration Form",
    font=("Arial", 22, "bold")
).grid(
    row=0,
    column=0,
    columnspan=2,
    pady=30
)

# Name
tk.Label(
    window,
    text="Name:"
).grid(row=1, column=0, padx=20, pady=10, sticky="e")

tk.Entry(
    window,
    width=35
).grid(row=1, column=1, padx=20, pady=10, sticky="w")

# Email
tk.Label(
    window,
    text="Email:"
).grid(row=2, column=0, padx=20, pady=10, sticky="e")

tk.Entry(
    window,
    width=35
).grid(row=2, column=1, padx=20, pady=10, sticky="w")

# Phone
tk.Label(
    window,
    text="Phone:"
).grid(row=3, column=0, padx=20, pady=10, sticky="e")

tk.Entry(
    window,
    width=35
).grid(row=3, column=1, padx=20, pady=10, sticky="w")

# Buttons
tk.Button(
    window,
    text="Register",
    width=15
).grid(
    row=4,
    column=0,
    columnspan=2,
    pady=25
)

window.mainloop()
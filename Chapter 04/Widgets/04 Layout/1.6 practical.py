import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Login")
window.geometry("600x350")

# Create login frame
login_frame = tk.Frame(
    window,
    padx=30,
    pady=30
)

# Heading
tk.Label(
    login_frame,
    text="Login",
    font=("Arial", 22, "bold")
).grid(
    row=0,
    column=0,
    columnspan=2,
    pady=20
)

# Username
tk.Label(
    login_frame,
    text="Username:"
).grid(row=1, column=0, padx=10, pady=10)

tk.Entry(
    login_frame,
    width=30
).grid(row=1, column=1, padx=10, pady=10)

# Password
tk.Label(
    login_frame,
    text="Password:"
).grid(row=2, column=0, padx=10, pady=10)

tk.Entry(
    login_frame,
    width=30,
    show="*"
).grid(row=2, column=1, padx=10, pady=10)

# Login button
tk.Button(
    login_frame,
    text="Login"
).grid(
    row=3,
    column=1,
    pady=20
)

# Display frame
login_frame.pack(pady=30)

window.mainloop()
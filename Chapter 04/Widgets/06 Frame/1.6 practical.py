import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Login")
window.geometry("600x400")
window.configure(bg="white")

# Login frame
login_frame = tk.Frame(
    window,
    bg="white",
    padx=40,
    pady=30,
    bd=2,
    relief="solid"
)

# Heading
tk.Label(
    login_frame,
    text="Login",
    font=("Arial", 24, "bold"),
    bg="white"
).grid(
    row=0,
    column=0,
    columnspan=2,
    pady=20
)

# Username
tk.Label(
    login_frame,
    text="Username:",
    bg="white"
).grid(row=1, column=0, padx=10, pady=10)

tk.Entry(
    login_frame,
    width=30
).grid(row=1, column=1, padx=10, pady=10)

# Password
tk.Label(
    login_frame,
    text="Password:",
    bg="white"
).grid(row=2, column=0, padx=10, pady=10)

tk.Entry(
    login_frame,
    width=30,
    show="*"
).grid(row=2, column=1, padx=10, pady=10)

# Login button
tk.Button(
    login_frame,
    text="Login",
    width=15
).grid(
    row=3,
    column=0,
    columnspan=2,
    pady=20
)

# Display frame
login_frame.pack(pady=50)

window.mainloop()
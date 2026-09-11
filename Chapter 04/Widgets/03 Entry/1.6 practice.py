import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

# Window setup
window.title("Login Form")
window.geometry("500x350")


# Username label
username_label = tk.Label(
    window,
    text="Username:"
)

# Username entry
username_entry = tk.Entry(
    window,
    width=30
)


# Password label
password_label = tk.Label(
    window,
    text="Password:"
)

# Password entry
password_entry = tk.Entry(
    window,
    width=30,
    show="*"
)


# Login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "":
        messagebox.showerror(
            "Error",
            "Please enter username"
        )
        return

    if password == "":
        messagebox.showerror(
            "Error",
            "Please enter password"
        )
        return

    if username == "admin" and password == "1234":
        messagebox.showinfo(
            "Success",
            "Login successful!"
        )
    else:
        messagebox.showerror(
            "Error",
            "Invalid username or password"
        )


# Login button
login_button = tk.Button(
    window,
    text="Login",
    width=15,
    command=login
)

# Display widgets
username_label.pack(pady=10)
username_entry.pack(pady=5)

password_label.pack(pady=10)
password_entry.pack(pady=5)

login_button.pack(pady=20)

window.mainloop()
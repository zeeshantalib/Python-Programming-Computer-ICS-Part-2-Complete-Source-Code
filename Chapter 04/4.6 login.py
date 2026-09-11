import tkinter as tk
from tkinter import messagebox

# Create main window
window = tk.Tk()
window.title("Login Form")
window.geometry("300x200")


# Function to check login
def check_login():
    username = entry_user.get()
    password = entry_pass.get()

    # Simple check
    if username == "admin" and password == "1234":
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


# Username label and entry
tk.Label(window, text="Username").pack()
entry_user = tk.Entry(window)
entry_user.pack()

# Password label and entry
tk.Label(window, text="Password").pack()
entry_pass = tk.Entry(window, show="*")
entry_pass.pack()

# Login button
tk.Button(window, text="Login", command=check_login).pack(pady=10)

# Run application
window.mainloop()
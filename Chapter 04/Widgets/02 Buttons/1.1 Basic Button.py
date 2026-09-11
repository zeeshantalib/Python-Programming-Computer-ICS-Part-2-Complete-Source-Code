import tkinter as tk
window = tk.Tk()

# Window setup
window.title("Button - Basic Example")
window.geometry("500x300")

# Button function
def say_hello():
    print("Hello, Tkinter!")

# Create button
button = tk.Button(
    window,
    text="Click Me",
    command=say_hello
)

# Display button
button.pack(pady=100)
window.mainloop()
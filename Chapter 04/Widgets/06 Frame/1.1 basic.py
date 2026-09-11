import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Basic Frame")
window.geometry("600x400")

# Create frame
frame = tk.Frame(window)

# Display frame
frame.pack(pady=50)

# Create widgets inside frame
tk.Label(
    frame,
    text="Hello, Frame!"
).pack(pady=10)

tk.Button(
    frame,
    text="Click Me"
).pack(pady=10)

window.mainloop()
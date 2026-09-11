import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Basic Label")
window.geometry("500x300")

# Create label
label = tk.Label(
    window,
    text="Hello, Tkinter!"
)

# Display label
label.pack(pady=100)

window.mainloop()
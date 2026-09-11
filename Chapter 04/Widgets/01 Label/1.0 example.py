import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Label Example")
window.geometry("600x400")
window.configure(bg="white")

# Create label
label = tk.Label(window)

# Set label text
label.config(text="Welcome to Tkinter")

# Set text font
label.config(font=("Arial", 20, "bold"))

# Set text color
label.config(fg="blue")

# Set background color
label.config(bg="white")

# Set label width
label.config(width=25)

# Set label height
label.config(height=2)

# Set text alignment
label.config(anchor="center")

# Set text justification
label.config(justify="center")

# Set border width
label.config(bd=2)

# Set border style
label.config(relief="solid")

# Set internal horizontal padding
label.config(padx=10)

# Set internal vertical padding
label.config(pady=5)

# Set cursor
label.config(cursor="hand2")

# Set text wrapping
label.config(wraplength=300)

# Set label position
label.pack(pady=50)

# Change label text
label.config(text="Hello, Zeeshan!")

# Get label text
print("Label Text:", label.cget("text"))

# Get label font
print("Label Font:", label.cget("font"))

# Get label foreground color
print("Label Color:", label.cget("fg"))

# Start application
window.mainloop()
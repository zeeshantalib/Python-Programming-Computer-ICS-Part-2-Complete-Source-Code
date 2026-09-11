import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Entry Example")
window.geometry("600x400")
window.configure(bg="white")

# Create entry
entry = tk.Entry(window)

# Set default text
entry.insert(0, "Enter your name")

# Set text font
entry.config(font=("Arial", 18, "bold"))

# Set text color
entry.config(fg="blue")

# Set background color
entry.config(bg="white")

# Set entry width
entry.config(width=30)

# Set border width
entry.config(bd=3)

# Set border style
entry.config(relief="solid")

# Set text alignment
entry.config(justify="center")

# Set internal horizontal padding
entry.config(padx=10)

# Set internal vertical padding
entry.config(pady=5)

# Set cursor
entry.config(cursor="xterm")

# Set cursor color
entry.config(insertbackground="red")

# Set cursor width
entry.config(insertwidth=2)

# Set cursor blink speed
entry.config(insertontime=600)

# Set cursor blink off time
entry.config(insertofftime=300)

# Set selected text background
entry.config(selectbackground="blue")

# Set selected text color
entry.config(selectforeground="white")

# Set selection border width
entry.config(selectborderwidth=2)

# Set password character
# entry.config(show="*")

# Set entry state
entry.config(state="normal")

# Set disabled text color
entry.config(disabledforeground="gray")

# Set disabled background color
entry.config(disabledbackground="lightgray")

# Set entry position
entry.pack(pady=100)

# Get entry text
print("Entry Text:", entry.get())

# Get entry font
print("Entry Font:", entry.cget("font"))

# Get entry foreground color
print("Entry Color:", entry.cget("fg"))

# Get entry background color
print("Entry Background:", entry.cget("bg"))

# Get entry width
print("Entry Width:", entry.cget("width"))

# Start application
window.mainloop()
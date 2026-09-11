import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Button Example")
window.geometry("600x400")
window.configure(bg="white")

# Button function
def button_click():
    print("Button clicked!")

# Create button
button = tk.Button(window)

# Set button text
button.config(text="Click Me")

# Set text font
button.config(font=("Arial", 20, "bold"))

# Set text color
button.config(fg="white")

# Set background color
button.config(bg="blue")

# Set button width
button.config(width=20)

# Set button height
button.config(height=2)

# Set text alignment
button.config(anchor="center")

# Set text justification
button.config(justify="center")

# Set border width
button.config(bd=2)

# Set border style
button.config(relief="raised")

# Set internal horizontal padding
button.config(padx=10)

# Set internal vertical padding
button.config(pady=5)

# Set cursor
button.config(cursor="hand2")

# Set active background color
button.config(activebackground="darkblue")

# Set active text color
button.config(activeforeground="white")

# Set disabled state
button.config(state="normal")

# Set button command
button.config(command=button_click)

# Set button position
button.pack(pady=50)

# Change button text
button.config(text="Hello, Zeeshan!")

# Get button text
print("Button Text:", button.cget("text"))

# Get button font
print("Button Font:", button.cget("font"))

# Get button foreground color
print("Button Color:", button.cget("fg"))

# Start application
window.mainloop()
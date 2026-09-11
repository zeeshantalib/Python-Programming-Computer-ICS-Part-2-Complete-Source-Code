import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Simple GUI Example")
window.geometry("300x200")

# Function to handle button click (event)
def on_click():
    label.config(text="Button Clicked!")

# Create a label
label = tk.Label(window, text="Welcome to Tkinter")
label.pack(pady=10)

# Create an entry field
entry = tk.Entry(window)
entry.pack(pady=10)

# Create a button
button = tk.Button(window, text="Click Me", command=on_click)
button.pack(pady=10)

# Run the application
window.mainloop()
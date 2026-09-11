import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Basic Layout")
window.geometry("500x300")

# Create widgets
label = tk.Label(window, text="Hello Tkinter")
button = tk.Button(window, text="Click Me")

# Display widgets
label.pack()
button.pack()

window.mainloop()
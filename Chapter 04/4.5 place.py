import tkinter as tk

# Create main window
window = tk.Tk()
window.title("place()")
window.geometry("300x220")

# Create buttons
button1 = tk.Button(window, text="Button 1", width=10)
button2 = tk.Button(window, text="Button 2", width=10)
button3 = tk.Button(window, text="Button 3", width=10)

# Arrange buttons using place()
button1.place(x=30, y=40)
button2.place(x=170, y=85)
button3.place(x=30, y=140)

# Run the application
window.mainloop()
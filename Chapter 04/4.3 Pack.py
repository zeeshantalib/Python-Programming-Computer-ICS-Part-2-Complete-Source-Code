import tkinter as tk

# Create main window
window = tk.Tk()
window.title("pack()")
window.geometry("300x220")

# Create buttons
button1 = tk.Button(window, text="Button 1", width=12)
button2 = tk.Button(window, text="Button 2", width=12)
button3 = tk.Button(window, text="Button 3", width=12)

# Arrange buttons using pack()
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)

# Run the application
window.mainloop()
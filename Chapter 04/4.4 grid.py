import tkinter as tk

# Create main window
window = tk.Tk()
window.title("grid()")
window.geometry("300x220")

# Create buttons
button1 = tk.Button(window, text="Button 1", width=10)
button2 = tk.Button(window, text="Button 2", width=10)
button3 = tk.Button(window, text="Button 3", width=24)

# Arrange buttons using grid()
button1.grid(row=0, column=0, padx=10, pady=20)
button2.grid(row=0, column=1, padx=10, pady=20)

# Button 3 spans two columns
button3.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Keep content centered
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Run the application
window.mainloop()
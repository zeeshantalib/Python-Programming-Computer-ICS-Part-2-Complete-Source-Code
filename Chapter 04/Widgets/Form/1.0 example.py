
import tkinter as tk

window = tk.Tk()

# Create window
window.title("My First Tkinter Program")

# Set window size
window.geometry("500x300")

# Set background color
window.configure(bg="green")

# Allow window resizing
window.resizable(True, True)

# Set minimum window size
window.minsize(400, 250)

# Set maximum window size
window.maxsize(800, 600)

# Set window icon
# window.iconbitmap("icon.ico")

# Set window transparency
window.attributes("-alpha", 0.9)

# Keep window on top
window.attributes("-topmost", True)

# Set window state
window.state("normal")

# Update window
window.update()

# Get window width
print("Window Width:", window.winfo_width())

# Get window height
print("Window Height:", window.winfo_height())

# Get screen width
print("Screen Width:", window.winfo_screenwidth())

# Get screen height
print("Screen Height:", window.winfo_screenheight())

# Run application
window.mainloop()

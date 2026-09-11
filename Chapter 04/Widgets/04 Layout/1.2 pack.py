import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Pack Layout")
window.geometry("600x400")

# Create buttons
top = tk.Button(window, text="Top")
bottom = tk.Button(window, text="Bottom")
left = tk.Button(window, text="Left")
right = tk.Button(window, text="Right")

# Position widgets
top.pack(side="top", pady=10)
bottom.pack(side="bottom", pady=10)
left.pack(side="left", padx=10)
right.pack(side="right", padx=10)

window.mainloop()
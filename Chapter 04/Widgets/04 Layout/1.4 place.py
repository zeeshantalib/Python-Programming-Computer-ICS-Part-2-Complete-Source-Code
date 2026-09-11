import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Place Layout")
window.geometry("600x400")

# Create widgets
label = tk.Label(window, text="Username:")
entry = tk.Entry(window, width=30)
button = tk.Button(window, text="Login")

# Position widgets
label.place(x=100, y=80)
entry.place(x=180, y=80)
button.place(x=250, y=140)

window.mainloop()
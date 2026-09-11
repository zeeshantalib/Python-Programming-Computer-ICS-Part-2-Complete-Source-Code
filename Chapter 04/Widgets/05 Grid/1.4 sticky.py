import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Grid Sticky")
window.geometry("600x350")

# Create widgets
label = tk.Label(
    window,
    text="Username:",
    bg="lightgray"
)

entry = tk.Entry(window)

# Position widgets
label.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky="e"
)

entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky="ew"
)

window.mainloop()
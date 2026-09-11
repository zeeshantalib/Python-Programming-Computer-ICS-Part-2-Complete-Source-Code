import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Grid Padding")
window.geometry("600x350")

# Create widgets
label = tk.Label(
    window,
    text="Name:",
    bg="lightgray"
)

entry = tk.Entry(window, width=30)

# External padding
label.grid(
    row=0,
    column=0,
    padx=20,
    pady=20
)

entry.grid(
    row=0,
    column=1,
    padx=20,
    pady=20
)

window.mainloop()
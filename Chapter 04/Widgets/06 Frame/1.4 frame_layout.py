import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Frame Layout")
window.geometry("600x400")

# Create form frame
form_frame = tk.Frame(
    window,
    padx=30,
    pady=30
)

# Name
tk.Label(
    form_frame,
    text="Name:"
).grid(row=0, column=0, padx=10, pady=10)

tk.Entry(
    form_frame,
    width=30
).grid(row=0, column=1, padx=10, pady=10)

# Email
tk.Label(
    form_frame,
    text="Email:"
).grid(row=1, column=0, padx=10, pady=10)

tk.Entry(
    form_frame,
    width=30
).grid(row=1, column=1, padx=10, pady=10)

# Button
tk.Button(
    form_frame,
    text="Submit"
).grid(
    row=2,
    column=1,
    pady=20
)

# Display frame
form_frame.pack(pady=40)

window.mainloop()
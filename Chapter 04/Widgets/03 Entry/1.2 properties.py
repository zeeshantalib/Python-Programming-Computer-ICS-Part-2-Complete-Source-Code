import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Entry Properties")
window.geometry("600x400")
window.configure(bg="white")


# Create entry
entry = tk.Entry(
    window,
    font=("Arial", 16),
    fg="blue",
    bg="lightgray",
    width=30,
    bd=3,
    relief="solid",
    justify="center",
    insertbackground="red",
    insertwidth=2,
    cursor="xterm",
    show=""
)

# Display entry
entry.pack(pady=100)

window.mainloop()
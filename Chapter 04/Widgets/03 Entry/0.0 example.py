import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Entry Example")
window.geometry("600x400")
window.configure(bg="white")

# Create entry with properties
entry = tk.Entry(
    window,
    font=("Arial", 18, "bold"),
    fg="blue",
    bg="white",
    width=30,
    bd=3,
    relief="solid",
    justify="center",
    cursor="xterm",
    insertbackground="red",
    selectbackground="blue",
    selectforeground="white",
    show=""
)

# Insert default text
entry.insert(0, "Enter your name")

# Display entry
entry.pack(pady=100)

# Get entry values
print("Text:", entry.get())
print("Font:", entry.cget("font"))
print("Color:", entry.cget("fg"))
print("Background:", entry.cget("bg"))

# Start application
window.mainloop()
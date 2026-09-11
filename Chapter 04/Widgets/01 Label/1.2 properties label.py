import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Label Properties")
window.geometry("600x400")
window.configure(bg="white")

# Create label
label = tk.Label(
    window,
    text="Welcome to Tkinter",
    font=("Arial", 20, "bold"),
    fg="blue",
    bg="white",
    width=25,
    height=3,
    padx=10,
    pady=10,
    bd=3,
    relief="solid",
    anchor="center",
    justify="center",
    cursor="hand2",
    wraplength=300
)

# Display label
label.pack(pady=80)

window.mainloop()
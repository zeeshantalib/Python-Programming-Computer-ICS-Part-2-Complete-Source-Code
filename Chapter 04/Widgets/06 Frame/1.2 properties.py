import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Frame Properties")
window.geometry("600x400")
window.configure(bg="white")

# Create frame with properties
frame = tk.Frame(
    window,
    bg="lightblue",
    width=400,
    height=200,
    bd=3,
    relief="solid",
    padx=20,
    pady=20,
    cursor="hand2"
)

# Prevent automatic resizing
frame.pack_propagate(False)

# Display frame
frame.pack(pady=80)

# Add widget
tk.Label(
    frame,
    text="Frame Example",
    font=("Arial", 20, "bold"),
    bg="lightblue"
).pack()

window.mainloop()
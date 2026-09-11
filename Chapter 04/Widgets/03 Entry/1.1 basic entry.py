import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Basic Entry")
window.geometry("500x300")


# Create label
label = tk.Label(
    window,
    text="Enter your name:"
)

# Create entry
entry = tk.Entry(
    window
)

# Display widgets
label.pack(pady=20)
entry.pack(pady=10)

window.mainloop()
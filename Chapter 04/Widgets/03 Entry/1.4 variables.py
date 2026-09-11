import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Entry Variables")
window.geometry("500x350")


# Create variable
name = tk.StringVar()


# Create label
label = tk.Label(
    window,
    text="Enter your name:"
)

# Create entry
entry = tk.Entry(
    window,
    textvariable=name,
    width=30
)


# Show value
def show_name():
    result.config(text=f"Hello, {name.get()}!")


# Result label
result = tk.Label(
    window,
    text=""
)

# Button
button = tk.Button(
    window,
    text="Submit",
    command=show_name
)

# Display widgets
label.pack(pady=20)
entry.pack(pady=10)
button.pack(pady=20)
result.pack(pady=10)

window.mainloop()
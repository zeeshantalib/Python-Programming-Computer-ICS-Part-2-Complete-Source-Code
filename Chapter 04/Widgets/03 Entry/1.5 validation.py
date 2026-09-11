import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Entry Validation")
window.geometry("500x350")


# Create entry
entry = tk.Entry(
    window,
    width=30
)


# Validate input
def validate():
    name = entry.get()

    if name == "":
        result.config(
            text="Please enter your name"
        )
    else:
        result.config(
            text=f"Welcome, {name}!"
        )


# Result label
result = tk.Label(
    window,
    text=""
)

# Submit button
button = tk.Button(
    window,
    text="Submit",
    command=validate
)

# Display widgets
entry.pack(pady=50)
button.pack(pady=10)
result.pack(pady=20)

window.mainloop()
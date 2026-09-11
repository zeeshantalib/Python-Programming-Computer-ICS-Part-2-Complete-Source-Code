import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Dynamic Label")
window.geometry("500x300")


# Change label text
def change_text():
    label.config(text="Text has been changed!")


# Create label
label = tk.Label(
    window,
    text="Original Text",
    font=("Arial", 18)
)

# Create button
button = tk.Button(
    window,
    text="Change Text",
    command=change_text
)

# Display widgets
label.pack(pady=50)
button.pack()

window.mainloop()
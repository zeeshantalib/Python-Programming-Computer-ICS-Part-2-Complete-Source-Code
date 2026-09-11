import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Multiple Buttons")
window.geometry("500x300")


# Button functions
def save():
    print("Save clicked")


def delete():
    print("Delete clicked")


def cancel():
    print("Cancel clicked")


# Create buttons
save_button = tk.Button(
    window,
    text="Save",
    command=save
)

delete_button = tk.Button(
    window,
    text="Delete",
    command=delete
)

cancel_button = tk.Button(
    window,
    text="Cancel",
    command=cancel
)

# Display buttons
save_button.pack(pady=10)
delete_button.pack(pady=10)
cancel_button.pack(pady=10)

window.mainloop()
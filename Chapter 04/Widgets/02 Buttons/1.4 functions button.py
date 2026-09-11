import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Button Functions")
window.geometry("500x300")


# Function with parameter
def show_message(message):
    print(message)


# Buttons
hello_button = tk.Button(
    window,
    text="Hello",
    command=lambda: show_message("Hello!")
)

welcome_button = tk.Button(
    window,
    text="Welcome",
    command=lambda: show_message("Welcome to Tkinter!")
)

exit_button = tk.Button(
    window,
    text="Exit",
    command=window.destroy
)

# Display buttons
hello_button.pack(pady=10)
welcome_button.pack(pady=10)
exit_button.pack(pady=10)

window.mainloop()
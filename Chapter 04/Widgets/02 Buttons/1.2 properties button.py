import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Button Properties")
window.geometry("600x400")
window.configure(bg="white")


# Button function
def click_button():
    print("Button clicked!")


# Create button
button = tk.Button(
    window,
    text="Click Me",
    command=click_button,
    font=("Arial", 16, "bold"),
    fg="white",
    bg="blue",
    width=15,
    height=2,
    padx=10,
    pady=5,
    bd=3,
    relief="raised",
    cursor="hand2",
    activebackground="darkblue",
    activeforeground="white"
)

# Display button
button.pack(pady=100)

window.mainloop()
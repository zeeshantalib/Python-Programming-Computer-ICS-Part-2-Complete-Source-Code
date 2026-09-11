import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Button Variables")
window.geometry("500x300")


# Create variable
count = tk.IntVar(value=0)


# Button function
def increase_count():
    count.set(count.get() + 1)


# Create label
label = tk.Label(
    window,
    textvariable=count,
    font=("Arial", 30)
)

# Create button
button = tk.Button(
    window,
    text="Increase",
    command=increase_count
)

# Display widgets
label.pack(pady=30)
button.pack()

window.mainloop()
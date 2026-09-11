import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Entry Methods")
window.geometry("500x350")


# Create entry
entry = tk.Entry(
    window,
    width=30
)

# Insert default text
entry.insert(0, "Enter your name")

# Get text
def get_text():
    print("Entered Text:", entry.get())


# Delete text
def delete_text():
    entry.delete(0, tk.END)


# Select all text
def select_text():
    entry.select_range(0, tk.END)


# Buttons
get_button = tk.Button(
    window,
    text="Get Text",
    command=get_text
)

delete_button = tk.Button(
    window,
    text="Delete Text",
    command=delete_text
)

select_button = tk.Button(
    window,
    text="Select All",
    command=select_text
)

# Display widgets
entry.pack(pady=30)
get_button.pack(pady=5)
delete_button.pack(pady=5)
select_button.pack(pady=5)

window.mainloop()
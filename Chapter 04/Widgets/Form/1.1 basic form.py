import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Basic Form")
window.geometry("500x350")

# Name label
name_label = tk.Label(
    window,
    text="Name"
)

# Name entry
name_entry = tk.Entry(
    window
)

# Email label
email_label = tk.Label(
    window,
    text="Email"
)

# Email entry
email_entry = tk.Entry(
    window
)

# Submit function
def submit():
    print("Name:", name_entry.get())
    print("Email:", email_entry.get())


# Submit button
submit_button = tk.Button(
    window,
    text="Submit",
    command=submit
)

# Display widgets
name_label.pack(pady=5)
name_entry.pack(pady=5)

email_label.pack(pady=5)
email_entry.pack(pady=5)

submit_button.pack(pady=20)

window.mainloop()
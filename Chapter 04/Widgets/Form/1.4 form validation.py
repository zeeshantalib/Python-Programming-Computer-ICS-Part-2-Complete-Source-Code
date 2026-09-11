import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Form Validation")
window.geometry("600x400")

# Create form frame
form_frame = tk.Frame(
    window,
    padx=30,
    pady=30
)

# Name
name_label = tk.Label(
    form_frame,
    text="Name:"
)

name_entry = tk.Entry(
    form_frame,
    width=30
)

# Email
email_label = tk.Label(
    form_frame,
    text="Email:"
)

email_entry = tk.Entry(
    form_frame,
    width=30
)

# Result label
result = tk.Label(
    form_frame,
    text=""
)

# Validate form
def submit():
    name = name_entry.get()
    email = email_entry.get()

    if name == "":
        result.config(text="Please enter your name")
        return

    if email == "":
        result.config(text="Please enter your email")
        return

    result.config(text="Form submitted successfully")


# Submit button
submit_button = tk.Button(
    form_frame,
    text="Submit",
    command=submit
)

# Display form
form_frame.pack(pady=40)

name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry.grid(row=0, column=1, padx=10, pady=10)

email_label.grid(row=1, column=0, padx=10, pady=10)
email_entry.grid(row=1, column=1, padx=10, pady=10)

submit_button.grid(row=2, column=1, pady=15)

result.grid(row=3, column=0, columnspan=2)

window.mainloop()
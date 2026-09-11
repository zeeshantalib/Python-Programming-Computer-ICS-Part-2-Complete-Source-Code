import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Nested Frames")
window.geometry("700x500")

# Main frame
main_frame = tk.Frame(
    window,
    bg="white"
)

# Top frame
top_frame = tk.Frame(
    main_frame,
    bg="lightblue",
    height=100
)

# Content frame
content_frame = tk.Frame(
    main_frame,
    bg="lightgray"
)

# Button frame
button_frame = tk.Frame(
    content_frame,
    bg="lightgray"
)

# Display frames
main_frame.pack(fill="both", expand=True)

top_frame.pack(fill="x")
content_frame.pack(fill="both", expand=True)
button_frame.pack(pady=30)

# Top content
tk.Label(
    top_frame,
    text="My Application",
    font=("Arial", 22, "bold"),
    bg="lightblue"
).pack(pady=30)

# Content
tk.Label(
    content_frame,
    text="Welcome!",
    font=("Arial", 18),
    bg="lightgray"
).pack(pady=50)

# Buttons
tk.Button(
    button_frame,
    text="Save",
    width=12
).pack(side="left", padx=10)

tk.Button(
    button_frame,
    text="Cancel",
    width=12
).pack(side="left", padx=10)

window.mainloop()
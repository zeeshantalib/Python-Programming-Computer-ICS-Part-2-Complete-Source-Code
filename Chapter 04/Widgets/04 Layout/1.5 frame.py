import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Frame Layout")
window.geometry("600x400")

# Create frames
top_frame = tk.Frame(window, bg="lightgray", height=80)
content_frame = tk.Frame(window)
bottom_frame = tk.Frame(window, bg="lightgray", height=60)

# Display frames
top_frame.pack(fill="x")
content_frame.pack(fill="both", expand=True)
bottom_frame.pack(fill="x")

# Top content
tk.Label(
    top_frame,
    text="My Application",
    font=("Arial", 20, "bold"),
    bg="lightgray"
).pack(pady=20)

# Content
tk.Button(
    content_frame,
    text="Click Me"
).pack(pady=50)

# Bottom content
tk.Label(
    bottom_frame,
    text="Status: Ready",
    bg="lightgray"
).pack(pady=15)

window.mainloop()
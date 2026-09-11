import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Multiple Frames")
window.geometry("700x500")

# Create frames
top_frame = tk.Frame(window, bg="lightblue", height=100)
middle_frame = tk.Frame(window, bg="white")
bottom_frame = tk.Frame(window, bg="lightgray", height=70)

# Display frames
top_frame.pack(fill="x")
middle_frame.pack(fill="both", expand=True)
bottom_frame.pack(fill="x")

# Add widgets
tk.Label(
    top_frame,
    text="Header",
    font=("Arial", 20, "bold"),
    bg="lightblue"
).pack(pady=30)

tk.Label(
    middle_frame,
    text="Main Content",
    font=("Arial", 18),
    bg="white"
).pack(pady=80)

tk.Label(
    bottom_frame,
    text="Footer",
    bg="lightgray"
).pack(pady=25)

window.mainloop()
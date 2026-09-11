import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Dashboard")
window.geometry("800x500")

# Header frame
header = tk.Frame(
    window,
    bg="lightblue",
    height=70
)

# Sidebar frame
sidebar = tk.Frame(
    window,
    bg="gray",
    width=180
)

# Content frame
content = tk.Frame(
    window,
    bg="white"
)

# Footer frame
footer = tk.Frame(
    window,
    bg="lightgray",
    height=50
)

# Display main frames
header.pack(fill="x")
footer.pack(side="bottom", fill="x")
sidebar.pack(side="left", fill="y")
content.pack(side="left", fill="both", expand=True)

# Header
tk.Label(
    header,
    text="Admin Dashboard",
    font=("Arial", 22, "bold"),
    bg="lightblue"
).pack(pady=20)

# Sidebar buttons
tk.Button(
    sidebar,
    text="Dashboard",
    width=15
).pack(pady=15)

tk.Button(
    sidebar,
    text="Users",
    width=15
).pack(pady=15)

tk.Button(
    sidebar,
    text="Settings",
    width=15
).pack(pady=15)

# Content
tk.Label(
    content,
    text="Welcome to Dashboard",
    font=("Arial", 22),
    bg="white"
).pack(pady=80)

# Footer
tk.Label(
    footer,
    text="Status: Ready",
    bg="lightgray"
).pack(pady=15)

window.mainloop()
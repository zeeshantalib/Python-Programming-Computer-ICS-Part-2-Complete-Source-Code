import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Tkinter Frames Example")
window.geometry("400x300")

# Create top frame
top_frame = tk.Frame(window, bg="lightblue", height=100)
top_frame.pack(fill="x")

# Create bottom frame
bottom_frame = tk.Frame(window, bg="lightgreen", height=200)
bottom_frame.pack(fill="both", expand=True)

# Add widgets to top frame
label_top = tk.Label(top_frame, text="Top Frame", bg="lightblue")
label_top.pack(pady=20)

# Add widgets to bottom frame
label_bottom = tk.Label(bottom_frame, text="Bottom Frame", bg="lightgreen")
label_bottom.pack(pady=50)

# Run the application
window.mainloop()
import tkinter as tk

window = tk.Tk()

# Window setup
window.title("Grid Basic")
window.geometry("500x300")

# Create widgets
label1 = tk.Label(window, text="Name:")
entry1 = tk.Entry(window)

label2 = tk.Label(window, text="Email:")
entry2 = tk.Entry(window)

# Position widgets
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)

label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)

window.mainloop()
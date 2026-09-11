import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Main Window
window = tk.Tk()
window.title("Tkinter Widgets Example")
window.geometry("700x700")

# ==========================
# Label
# ==========================
label = tk.Label(window, text="This is a Label")
label.pack(pady=5)

# ==========================
# Button
# ==========================
button = tk.Button(window, text="Click Me")
button.pack(pady=5)

# ==========================
# Entry
# ==========================
entry = tk.Entry(window)
entry.pack(pady=5)

# ==========================
# Text
# ==========================
text = tk.Text(window, width=30, height=4)
text.pack(pady=5)

# ==========================
# Checkbutton
# ==========================
check_var = tk.IntVar()

checkbutton = tk.Checkbutton(
    window,
    text="Python",
    variable=check_var
)

checkbutton.pack(pady=5)

# ==========================
# Radiobutton
# ==========================
gender = tk.StringVar()

radio1 = tk.Radiobutton(
    window,
    text="Male",
    variable=gender,
    value="Male"
)

radio2 = tk.Radiobutton(
    window,
    text="Female",
    variable=gender,
    value="Female"
)

radio1.pack()
radio2.pack()

# ==========================
# Listbox
# ==========================
listbox = tk.Listbox(window)

listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")

listbox.pack(pady=5)

# ==========================
# Combobox
# ==========================
combobox = ttk.Combobox(window)

combobox["values"] = (
    "Computer Science",
    "Mathematics",
    "Physics"
)

combobox.pack(pady=5)

# ==========================
# Spinbox
# ==========================
spinbox = tk.Spinbox(
    window,
    from_=1,
    to=10
)

spinbox.pack(pady=5)

# ==========================
# Scale
# ==========================
scale = tk.Scale(
    window,
    from_=0,
    to=100,
    orient="horizontal"
)

scale.pack(pady=5)

# ==========================
# LabelFrame
# ==========================
labelframe = tk.LabelFrame(
    window,
    text="Student Information"
)

labelframe.pack(pady=10)

tk.Label(
    labelframe,
    text="Inside LabelFrame"
).pack()

# ==========================
# Frame
# ==========================
frame = tk.Frame(
    window,
    bg="lightgray",
    width=200,
    height=50
)

frame.pack(pady=10)

# ==========================
# Progressbar
# ==========================
progress = ttk.Progressbar(
    window,
    length=200,
    mode="determinate"
)

progress["value"] = 70

progress.pack(pady=5)

# ==========================
# Treeview
# ==========================
tree = ttk.Treeview(
    window,
    columns=("Name", "Age"),
    show="headings"
)

tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

tree.insert("", tk.END, values=("Ali", 20))
tree.insert("", tk.END, values=("Ahmed", 22))

tree.pack(pady=10)

# ==========================
# Notebook (Tabs)
# ==========================
notebook = ttk.Notebook(window)

tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)

notebook.add(tab1, text="Home")
notebook.add(tab2, text="About")

notebook.pack(fill="both", expand=True, pady=10)

# ==========================
# Main Loop
# ==========================
window.mainloop()
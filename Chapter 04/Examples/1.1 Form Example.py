import tkinter as tk
window = tk.Tk()

window.title("My First Tkinter Program")
window.geometry("500x300")
window.configure(bg="white")
window.resizable(False, False)

window.minsize(400, 250)
window.maxsize(800, 600)

#window.iconbitmap("icon.ico")
window.mainloop()

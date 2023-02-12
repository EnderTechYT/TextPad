# Import Libraries
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Setup Variables


# Do nothing
def dn():
    return

# Create window
root = tk.Tk()
root.geometry("640x480")
root.resizable(False, False)
root.title("Entry Key")
root.protocol("WM_DELETE_WINDOW", dn)
root.config(bg="white")

# Widgets Creation
tk.Label(root, text="Type out any one code out of 50.", bg="white", font="Calibri 14").pack()
code = tk.Entry(root, font="Consolas 14", highlightthickness=2, highlightcolor="Black")
code.pack(pady=10)
cte = ttk.Button(root, text="Proceed", command=root.destroy)
cte.pack()

# Start Program
root.mainloop()

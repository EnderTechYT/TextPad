# Import Libraries
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askyesno
# Variable Setup
title = "TextPad"
isdm = 0
# Function To Open File
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"{title} - {filepath}")
# Function To Save File
def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"{title} - {filepath}")
# Function To Toggle Dark Mode
def toggle_dm():
    global isdm
    if isdm == 0:
        # Dark Mode
        txt_edit.config(bg="black", fg="white", insertbackground="white")
        isdm = 1
    elif isdm == 1:
        # Light Mode
        txt_edit.config(bg="white", fg="black", insertbackground="black")
        isdm = 0
# Function To Exit Program
def leave():
    ans = askyesno("Exit?", "Exit TextPad?")
    if ans:
        window.destroy()
# Window Setup
window = tk.Tk()
window.resizable(False, False)
window.title(title)
window.rowconfigure(0, minsize=550, weight=1)
window.columnconfigure(1, minsize=600, weight=1)
window.protocol("WM_DELETE_WINDOW", leave)
# Widget Setup
scroll_bar = tk.Scrollbar(window)
txt_edit = tk.Text(window, yscrollcommand=scroll_bar.set)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_dm = tk.Button(fr_buttons, text="Toggle Dark Mode", command=toggle_dm)
btn_exit = tk.Button(fr_buttons, text="Exit", command=leave)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_dm.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_exit.grid(row=3, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
scroll_bar.grid(row=0, column=2, sticky="nese")
scroll_bar.config(command=txt_edit.yview, orient="vertical")
# Icon Setup
icon = tk.PhotoImage(file = "favicon.png")
window.iconphoto(False, icon)
# Start Program
window.mainloop()

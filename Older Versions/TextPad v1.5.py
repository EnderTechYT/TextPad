# Import Libraries
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askyesno

# Program Setup
title = "TextPad" # App Title
isdm = 0 # Dark Mode
isfs = 0 # Fullscreen Mode
ver = "1.5" # Version

# Function To Open File
def open_file(code = 0):
    global title
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    title = f"TextPad - {filepath}"
    window.title(title)

# Function To Save File
def save_file(code = 0):
    try:
        global title
        filelist = title.split(" ")[2:]
        path = ' '.join([str(idx) for idx in filelist])
        with open(path, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.truncate()
            output_file.write(text)
        title = f"TextPad - {path}"
        window.title(title)
    except:
        save_as_file()

# Function To Save File As
def save_as_file(code = 0):
    global title
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    title = f"TextPad - {filepath}"
    window.title(title)

# Function To Toggle Dark Mode
def toggle_dm(code = 0):
    global isdm
    if isdm == 0:
        # Dark Mode
        txt_edit.config(bg="black", fg="white", insertbackground="white")
        isdm = 1
    elif isdm == 1:
        # Light Mode
        txt_edit.config(bg="white", fg="black", insertbackground="black")
        isdm = 0

# Function To Toogle Fullscreen Mode
def toggle_fs(code = 0):
    global isfs
    if isfs == 0:
        # Enter Fullscreen
        window.attributes("-fullscreen", True)
        isfs = 1
    elif isfs == 1:
        # Exit Fullscreen
        window.attributes("-fullscreen", False)
        isfs = 0

# Function To Show About
def showinfo():
    about = tk.Toplevel(bg="white")
    about.wm_title("About TextPad")
    about.wm_geometry("512x512")
    about.resizable(False, False)
    about.grab_set()
    header = tk.Label(about, text="TextPad", fg="black", bg="white", font=('Consolas', 35))
    version = tk.Label(about, text=f"Version {ver}", bg="white")
    about_txt_1 = tk.Label(about, text="TextPad is an open-source text editor by R.Rishikeshavan.", bg="white")
    about_txt_2 = tk.Label(about, text="This Project has started in Jan 24, 2022. Hardcoded in Python.", bg="white")
    header.pack(pady=20)
    version.pack(anchor="nw", padx=10)
    about_txt_1.pack(anchor="nw", padx=10, pady=10)
    about_txt_1.pack(anchor="nw", padx=10)
    about.iconphoto(False, icon)

# Function To Exit Program
def leave(code = 0):
    ans = askyesno("Exit?", "Exit TextPad?")
    if ans:
        window.destroy()

# Function To Setup Find Window (Similar To About Window)
def showfind(code = 0):
    find = tk.Toplevel()
    find.wm_title("Find")
    find.wm_geometry("512x232")
    find.resizable(False, False)
    find.grab_set()
    fram = ttk.Frame(find)
    tk.Label(fram,text="Text to find:").pack(side=tk.LEFT)
    edit = ttk.Entry(fram)
    edit.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    edit.focus_set()
    butt = ttk.Button(fram, text="Find") 
    butt.pack(side=tk.RIGHT)
    fram.pack(side=tk.TOP)
    find.iconphoto(False, icon)
    def get():
        txt_edit.tag_remove("found", '1.0', tk.END)
        s = edit.get()
        if s:
            idx = "1.0"
            while 1:
                idx = txt_edit.search(s, idx, nocase=1, stopindex=tk.END)
                if not idx: break
                lastidx = "%s+%dc" % (idx, len(s))
                txt_edit.tag_add("found", idx, lastidx)
                idx = lastidx
            txt_edit.tag_config("found", foreground="black", background="yellow")
    def clear():
        if isdm == 0:
            txt_edit.tag_config("found", background="white")
            txt_edit.tag_remove("found", '1.0', tk.END)
        elif isdm == 1:
            txt_edit.tag_config("found", foreground="white", background="black")
            txt_edit.tag_remove("found", '1.0', tk.END)
        find.destroy()
    butt.config(command=get)
    find.protocol("WM_DELETE_WINDOW", clear)

# Function To Copy Text
def copyup():
    try:
        window.clipboard_clear()
        window.clipboard_append(str(txt_edit.selection_get()))
        window.update()
    except:
        print("", end="") # Don't Do Anything

# Function To Paste Text
def pasteup():
    try:
        txt_edit.insert(tk.END, window.clipboard_get())
    except:
        print("", end="") # Don't Do Anything

# Fnction To Select All Text
def selectall():
    txt_edit.tag_add(tk.SEL, "1.0", tk.END)
    txt_edit.mark_set(tk.INSERT, "1.0")
    txt_edit.see(tk.INSERT)
    return "break"

# Function To Update The Cursor Position Detials
def rowcol(ev = None):
    r, c = txt_edit.index("insert").split(".")
    infobar["text"] = f"Ln: {r}\tCol: {c}"

# Window Setup
window = tk.Tk()
window.title(title)
window.minsize(800, 550)
window.rowconfigure(0, minsize=550, weight=1)
window.columnconfigure(1, minsize=600, weight=1)
window.bind('<Control-q>', leave)
window.bind('<Control-o>', open_file)
window.bind('<Control-s>', save_file)
window.bind('<Control-S>', save_as_file)
window.bind('<Control-f>', showfind)
window.bind('<Control-D>', toggle_dm)
window.bind('<F11>', toggle_fs)
window.protocol("WM_DELETE_WINDOW", leave)

# Widget Setup
scroll_bar = ttk.Scrollbar(window)
txt_edit = tk.Text(window, yscrollcommand=scroll_bar.set)
txt_edit.grid(row=0, column=1, sticky="nsew")
infobar = tk.Label(window)
infobar.grid(row=1, column=1, sticky="nsew")
txt_edit.event_add("<<REACT>>", *("<Motion>", "<ButtonRelease>", "<KeyPress>", "<KeyRelease>"))
b = txt_edit.bind("<<REACT>>", rowcol)
rowcol()
scroll_bar.grid(row=0, column=2, sticky="nese")
scroll_bar.config(command=txt_edit.yview, orient="vertical")
menubar = tk.Menu(window)
file = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command=None, accelerator="Ctrl+N")
file.add_command(label ='Open...', command=open_file, accelerator="Ctrl+O")
file.add_command(label ='Save', command=save_file, accelerator="Ctrl+S")
file.add_command(label ='Save As', command=save_as_file, accelerator="Ctrl+Shift+S")
file.add_separator()
file.add_command(label='Exit', command=leave, accelerator="Ctrl+Q")
edit = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Copy', command=copyup, accelerator="Ctrl+C")
edit.add_command(label='Paste', command=pasteup, accelerator="Ctrl+P")
edit.add_command(label='Select All', command=selectall, accelerator="Ctrl+A")
edit.add_command(label='Find...', command=showfind, accelerator="Ctrl+F")
options = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Options', menu=options)
options.add_command(label='Toggle Dark Mode', command=toggle_dm, accelerator="Ctrl+Shift+D")
options.add_command(label='Toggle Fullscreen Mode', command=toggle_fs, accelerator="F11")
about = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=about)
about.add_command(label ='About TextPad', command=showinfo)
window.config(menu=menubar)

# Icon Setup
icon = tk.PhotoImage(file = "favicon.png")
window.iconphoto(False, icon)

# Start Program
window.mainloop()

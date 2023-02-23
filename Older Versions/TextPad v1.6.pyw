# Import Libraries
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askyesno, showinfo
import os, json

# Get data from memory
rdata = open("Resources/data.txt", "r")
data = json.loads(rdata.read())
rdata.close()

# Program Setup
title = "TextPad" # App Title
isdm = data["darkscreen"] # Dark Mode
isfs = 0 # Fullscreen Mode
ver = "1.6" # Version
#font = "Courier New" # Font
font = data["font"] # Font
sfont = font # Default Preview Font
size = 10 # Size
# Fonts Available
fonts = ['System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier', 'MS Serif', 'MS Sans Serif', 'Small Fonts', 'Marlett', 'Arial',
    'Arabic Transparent', 'Arial Baltic', 'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Arial Black', 'Bahnschrift Light', 'Bahnschrift SemiLight',
    'Bahnschrift', 'Bahnschrift SemiBold', 'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiLight SemiConde', 'Bahnschrift SemiCondensed',
    'Bahnschrift SemiBold SemiConden', 'Bahnschrift Light Condensed', 'Bahnschrift SemiLight Condensed', 'Bahnschrift Condensed',
    'Bahnschrift SemiBold Condensed', 'Calibri', 'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Candara Light', 'Comic Sans MS',
    'Consolas', 'Constantia', 'Corbel', 'Corbel Light', 'Courier New', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR',
    'Courier New Greek', 'Courier New TUR', 'Ebrima', 'Franklin Gothic Medium', 'Gabriola', 'Gadugi', 'Georgia', 'Impact', 'Ink Free', 'Javanese Text',
    'Leelawadee UI', 'Leelawadee UI Semilight', 'Lucida Console', 'Lucida Sans Unicode', 'Malgun Gothic', '@Malgun Gothic', 'Malgun Gothic Semilight',
    '@Malgun Gothic Semilight', 'Microsoft Himalaya', 'Microsoft JhengHei', '@Microsoft JhengHei', 'Microsoft JhengHei UI', '@Microsoft JhengHei UI',
    'Microsoft JhengHei Light', '@Microsoft JhengHei Light', 'Microsoft JhengHei UI Light', '@Microsoft JhengHei UI Light', 'Microsoft New Tai Lue',
    'Microsoft PhagsPa', 'Microsoft Sans Serif', 'Microsoft Tai Le', 'Microsoft YaHei', '@Microsoft YaHei', 'Microsoft YaHei UI', '@Microsoft YaHei UI',
    'Microsoft YaHei Light', '@Microsoft YaHei Light', 'Microsoft YaHei UI Light', '@Microsoft YaHei UI Light', 'Microsoft Yi Baiti', 'MingLiU-ExtB',
    '@MingLiU-ExtB', 'PMingLiU-ExtB', '@PMingLiU-ExtB', 'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'Mongolian Baiti', 'MS Gothic', '@MS Gothic',
    'MS UI Gothic', '@MS UI Gothic', 'MS PGothic', '@MS PGothic', 'MV Boli', 'Myanmar Text', 'Nirmala UI', 'Nirmala UI Semilight', 'Palatino Linotype',
    'Segoe MDL2 Assets', 'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Black', 'Segoe UI Emoji', 'Segoe UI Historic', 'Segoe UI Light',
    'Segoe UI Semibold', 'Segoe UI Semilight', 'Segoe UI Symbol', 'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB', '@SimSun-ExtB', 'Sitka Small',
    'Sitka Text', 'Sitka Subheading', 'Sitka Heading', 'Sitka Display', 'Sitka Banner', 'Sylfaen', 'Symbol', 'Tahoma', 'Times New Roman',
    'Times New Roman Baltic', 'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Trebuchet MS',
    'Verdana', 'Webdings', 'Wingdings', 'Yu Gothic', '@Yu Gothic', 'Yu Gothic UI', '@Yu Gothic UI', 'Yu Gothic UI Semibold', '@Yu Gothic UI Semibold',
    'Yu Gothic Light', '@Yu Gothic Light', 'Yu Gothic UI Light', '@Yu Gothic UI Light', 'Yu Gothic Medium', '@Yu Gothic Medium', 'Yu Gothic UI Semilight',
    '@Yu Gothic UI Semilight', 'HoloLens MDL2 Assets', 'MT Extra', 'Arial Unicode MS', '@Arial Unicode MS', 'Century', 'Wingdings 2', 'Wingdings 3',
    'Tempus Sans ITC', 'Pristina', 'Papyrus', 'Mistral', 'Lucida Handwriting', 'Kristen ITC', 'Juice ITC', 'French Script MT', 'Freestyle Script',
    'Bradley Hand ITC', 'MS Outlook', 'Arial Narrow', 'Book Antiqua', 'Garamond', 'Monotype Corsiva', 'Century Gothic', 'Algerian', 'Baskerville Old Face',
    'Bauhaus 93', 'Bell MT', 'Berlin Sans FB', 'Bernard MT Condensed', 'Bodoni MT Poster Compressed', 'Britannic Bold', 'Broadway', 'Brush Script MT',
    'Californian FB', 'Centaur', 'Chiller', 'Colonna MT', 'Cooper Black', 'Footlight MT Light', 'Harlow Solid Italic', 'Harrington', 'High Tower Text',
    'Jokerman', 'Kunstler Script', 'Lucida Bright', 'Lucida Calligraphy', 'Lucida Fax', 'Magneto', 'Matura MT Script Capitals', 'Modern No. 20',
    'Niagara Engraved', 'Niagara Solid', 'Old English Text MT', 'Onyx', 'Parchment', 'Playbill', 'Poor Richard', 'Ravie', 'Informal Roman', 'Showcard Gothic',
    'Snap ITC', 'Stencil', 'Viner Hand ITC', 'Vivaldi', 'Vladimir Script', 'Wide Latin', 'Tw Cen MT', 'Tw Cen MT Condensed', 'Script MT Bold',
    'Rockwell Extra Bold', 'Rockwell Condensed', 'Rockwell', 'Rage Italic', 'Perpetua Titling MT', 'Perpetua', 'Palace Script MT', 'OCR A Extended',
    'Maiandra GD', 'Lucida Sans Typewriter', 'Lucida Sans', 'Imprint MT Shadow', 'Haettenschweiler', 'Goudy Stout', 'Goudy Old Style',
    'Gloucester MT Extra Condensed', 'Gill Sans Ultra Bold Condensed', 'Gill Sans Ultra Bold', 'Gill Sans MT Condensed', 'Gill Sans MT',
    'Gill Sans MT Ext Condensed Bold', 'Gigi', 'Franklin Gothic Medium Cond', 'Franklin Gothic Heavy', 'Franklin Gothic Demi Cond', 'Franklin Gothic Demi',
    'Franklin Gothic Book', 'Forte', 'Felix Titling', 'Eras Medium ITC', 'Eras Light ITC', 'Eras Demi ITC', 'Eras Bold ITC', 'Engravers MT', 'Elephant',
    'Edwardian Script ITC', 'Curlz MT', 'Copperplate Gothic Light', 'Copperplate Gothic Bold', 'Century Schoolbook', 'Castellar', 'Calisto MT',
    'Bookman Old Style', 'Bodoni MT Condensed', 'Bodoni MT Black', 'Bodoni MT', 'Blackadder ITC', 'Arial Rounded MT Bold', 'Agency FB', 'Bookshelf Symbol 7',
    'MS Reference Sans Serif', 'MS Reference Specialty', 'Berlin Sans FB Demi', 'Tw Cen MT Condensed Extra Bold']

# Function To Create New File
def new_file(code = 0):
    return

# Function To Edit Font
def showfont(code = 0):
    fontdialog = tk.Toplevel()
    fontdialog.wm_title("Select Font")
    fontdialog.wm_geometry("490x500")
    fontdialog.resizable(False, False)
    fontdialog.focus_set()
    fontdialog.grab_set()
    def tick():
        global font, sfont
        sfont = font
        for nfont in range(len(fonts)):
            flst.insert(nfont + 1, fonts[nfont])
        flst.select_set(fonts.index(font))
    def close(code = 0): fontdialog.destroy()
    def save(code = 0):
        global font, txt_edit, sfont, size
        try:
            font = flst.get(flst.curselection())
            txt_edit.config(font=(font, size))
            data["font"] = font
            ndata = json.dumps(data, indent=4)
            df = open("Resources/data.txt", "w")
            df.write(ndata)
            df.close()
            close()
        except:
            showinfo("Select a font", "You didn't select a font yet! Select a font to set.")
    def update(code = 0):
        global sfont, size
        try:
            sfont = flst.get(flst.curselection())
        except:
            print("", end="")
        ptxt.config(font=(sfont, size))
    flbl = ttk.LabelFrame(fontdialog, text="Font")
    fslbl = tk.Frame(flbl)
    flst = tk.Listbox(fslbl, height=15, width=25)
    flst.grid(row=0, column=0, pady=15)
    fslbl.grid(row=0, column=0, padx=10)
    flbl.grid(row=0, column=0, padx=15, pady=15)
    scbr = tk.Scrollbar(fslbl)
    scbr.grid(column=1, row=0, pady=15, sticky="nese")
    flst.config(yscrollcommand = scbr.set)
    scbr.config(command=flst.yview)
    tick()
    plbl = ttk.LabelFrame(fontdialog, text="Preview")
    ptxt = tk.Text(plbl, height=15, width=26, font=(sfont, size))
    ptxt.grid(row=0, column=0, padx=15, pady=15)
    ptxt.insert(tk.END,"ABCDEFGHIJKLMNOPQRSTUVWXYZ\n\nabcdefghijklmnopqrstuvwxyz\n\n1234567890\n\n`~!@#$%^&*()-_=+[]{}|?;:'\",.<>/\\")
    plbl.grid(row=0, column=1)
    flst.bind("<<ListboxSelect>>", update)
    okbtn = ttk.Button(fontdialog, text="Ok", command=save)
    cbtn = ttk.Button(fontdialog, text="Cancel", command=close)
    okbtn.grid(column=0, row=1, ipadx=5, ipady=2, pady=5)
    cbtn.grid(column=0, row=2, ipadx=5, ipady=2)
    fontdialog.bind("<Escape>", close)
    fontdialog.bind("<Return>", save)
    

# Function To Open File
def open_file(code = 0):
    global title
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    filename = os.path.basename(filepath)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    title = f"TextPad - {filepath}"
    window.title(title)

# Function To Save File
def save_file(code = 0):
    global title
    filelist = title.split(" ")[2:]
    path = ' '.join([str(idx) for idx in filelist])
    text = txt_edit.get(1.0, tk.END)
    result = os.system(f"echo {text} > {path}")
    #print(result)
    '''
    with open(path, "a") as output_file:
        output_file.truncate()
        output_file.write(text)
        output_file.close()
    '''
    title = f"TextPad - {path}"
    window.title(title)

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

# Function To Update Dark Mode
def update_dm():
    global isdm
    if isdm == 1:
        # Dark Mode
        txt_edit.config(bg="black", fg="white", insertbackground="white")
    elif isdm == 0:
        # Light Mode
        txt_edit.config(bg="white", fg="black", insertbackground="black")

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
    data["darkscreen"] = isdm
    ndata = json.dumps(data, indent=4)
    df = open("Resources/data.txt", "w")
    df.write(ndata)
    df.close()

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
def showabout():
    about = tk.Toplevel(bg="white")
    about.wm_title("About TextPad")
    about.wm_geometry("512x512")
    about.resizable(False, False)
    about.grab_set()
    about.focus_set()
    header = tk.Label(about, text="TextPad", fg="black", bg="white", font=('Consolas', 35))
    version = tk.Label(about, text=f"Version {ver}", bg="white")
    about_txt_1 = tk.Label(about, text="TextPad is an open-source text editor created by TechieKiddie.", bg="white")
    about_txt_2 = tk.Label(about, text="This Project has started in Jan 24, 2022. Programmed in Python 100%.", bg="white")
    header.pack(pady=20)
    version.pack(anchor="nw", padx=10)
    about_txt_1.pack(anchor="nw", padx=10, pady=10)
    about_txt_2.pack(anchor="nw", padx=10)

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
    find.focus_set()
    fram = ttk.Frame(find)
    tk.Label(fram,text="Text to find:").pack(side=tk.LEFT)
    edit = ttk.Entry(fram)
    edit.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    edit.focus_set()
    butt = ttk.Button(fram, text="Find") 
    butt.pack(side=tk.RIGHT)
    fram.pack(side=tk.TOP)
    def get():
        txt_edit.tag_remove("found", "1.0", tk.END)
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
            txt_edit.tag_remove("found", "1.0", tk.END)
        elif isdm == 1:
            txt_edit.tag_config("found", foreground="white", background="black")
            txt_edit.tag_remove("found", "1.0", tk.END)
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
window.bind('<Control-n>', new_file)
window.bind('<Control-o>', open_file)
window.bind('<Control-s>', save_file)
window.bind('<Control-S>', save_as_file)
window.bind('<Control-f>', showfind)
window.bind('<Control-D>', toggle_dm)
window.bind('<Control-h>', showfont)
window.bind('<F11>', toggle_fs)
window.protocol("WM_DELETE_WINDOW", leave)

# Widget Setup
scroll_bar = ttk.Scrollbar(window)
txt_edit = tk.Text(window, yscrollcommand=scroll_bar.set, font=(font, size))
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
menubar.add_cascade(label="File", menu = file)
file.add_command(label="New File", command=new_file, accelerator="Ctrl+N")
file.add_command(label="Open...", command=open_file, accelerator="Ctrl+O")
file.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file.add_command(label="Save As", command=save_as_file, accelerator="Ctrl+Shift+S")
file.add_separator()
file.add_command(label="Exit", command=leave, accelerator="Ctrl+Q")
edit = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Copy", command=copyup, accelerator="Ctrl+C")
edit.add_command(label="Paste", command=pasteup, accelerator="Ctrl+P")
edit.add_command(label="Select All", command=selectall, accelerator="Ctrl+A")
edit.add_command(label="Find...", command=showfind, accelerator="Ctrl+F")
options = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Options", menu=options)
options.add_command(label="Toggle Dark Mode", command=toggle_dm, accelerator="Ctrl+Shift+D")
options.add_command(label="Toggle Fullscreen Mode", command=toggle_fs, accelerator="F11")
options.add_command(label="Select Font", command=showfont, accelerator="Ctrl+H")
about = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=about)
about.add_command(label="About TextPad", command=showabout)
window.config(menu=menubar)
update_dm()

# Icon Setup
icon = tk.PhotoImage(file="Resources/favicon.png")
window.iconphoto(True, icon)

# Start Program
window.mainloop()

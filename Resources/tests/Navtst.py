import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('400x300')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='Personal')
notebook.add(frame2, text='Profile')

# add textbox to frames

txt1 = tk.Text(frame1, width=200, height=100)
txt2 = tk.Text(frame2, width=200, height=100)
txt1.pack()
txt2.pack()

# right click menu
m = tk.Menu(root, tearoff = 0)
m.add_command(label ="Rename tab")
  
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
        
    finally:
        m.grab_release()
  
txt1.bind("<Button-3>", do_popup)



root.mainloop()


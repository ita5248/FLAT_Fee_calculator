from tkinter import *
from tkinter import ttk
root = Tk()
l =ttk.Label(root, text="Starting...")
l.grid()
l.bind('<Enter>', lambda x: l.configure(text='Moved mouse inside'))
l.bind('<Leave>', lambda x: l.configure(text='Moved mouse outside'))
l.bind('<1>', lambda x: l.configure(text='Clicked left mouse button'))
l.bind('<Double-1>', lambda x: l.configure(text='Double clicked'))
l.bind('<B3-Motion>', lambda x: l.configure(text='right button drag to %d,%d' % (x.x, x.y)))
root.mainloop()
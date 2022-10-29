from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("700x350")


def clear_combobox():
  combobox.set('')

ingridient=('1','2','3')


var = StringVar()
combobox = ttk.Combobox(root, textvariable = var)
combobox['values'] = ingridient
combobox['state'] = 'readonly'
combobox.pack(fill='x',padx= 5, pady=5)


root.mainloop()
from tkinter import *
from tkinter import ttk
import pandas as pd

#обьявление таблиц
df = pd.DataFrame({
    'prod': ['Творог', 'Йогурт', 'Молоко', 'Каша'],
    'belk': [17.04, 143.5, 9.5, 45.5],
    'jir': [2724902, 17125191, 207600, 603628],
    'ugl':[1,2,3,4]
 },  #index=['t', 'y', 'm', 'k'])
)


#обьявление окна
root = Tk()
root.geometry("700x350")


def clear_combobox():
  combobox.set('')

ingridient=('1','2','3')


var = StringVar()
combobox = ttk.Combobox(root, textvariable = var)
combobox['values'] = df['prod']
combobox['state'] = 'readonly'
combobox.pack(fill='x',padx= 100, pady=100)



root.mainloop()
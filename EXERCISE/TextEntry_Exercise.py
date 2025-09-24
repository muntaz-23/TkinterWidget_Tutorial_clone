from textwrap import wrap
import tkinter as tk
from tkinter import ttk



#This section creates the Tkinter Window and adds the required elements to it
window = tk.Tk()
window.title('Tkinter Text Entry Wudget')
window.geometry('400x400')

#This is our Entry widget
string_var = tk.StringVar()
Text_entry = ttk.Entry(master = window,textvariable = string_var, font ='Calibri 24 bold', foreground = 'orange', justify = 'center', show = '8')

#Pack elements in frames ready to push onto form/window
Text_entry.pack()

#run the program to generate window with all the packed elements for user interaction
window.mainloop()
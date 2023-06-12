from tkinter import *
from tkinter import font
from define import *

from app import *

window =Tk()

app = App(window)

fontTitle = font.Font(family= "Stencil Std", size= 21)
fontText = font.Font(family= "Terminal", size= 12)

def show(name):
    label['background'] = name

def creat_button(name, index):
    Button(window, text = name ,font = fontText, padx=30, pady = 10, bg= name,width = 10, fg = 'black', command= lambda:show(name)).grid(row = 1, column = index, sticky='we', padx=30)

label = Label(window, text = 'HELLO', font=fontTitle, padx = 30, pady=10, bg = 'purple')
label.grid(row = 0, column= 0, columnspan=4, sticky='wse', padx = 30)
creat_button('green', 0)
creat_button('blue', 1)
creat_button('red', 2)
creat_button('yellow', 3)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)


window.mainloop()




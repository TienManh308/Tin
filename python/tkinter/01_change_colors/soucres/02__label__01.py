from tkinter import *
from tkinter import font
from define import *

from app import *
root = Tk()

app = App(root)

print(font.families())

font_title = font.Font(family ="Stencil Std", size = 40)
font_text = font.Font(family ="Terminal", size = 20)

labelTitle = Label(root, text = 'Title', font = font_title, bg = COLOR_RED, fg = COLOR_YELLOW, width=10).grid(row =1, column= 1)
labelText = Label(root, text = 'Text', font = font_text, bg = COLOR_YELLOW, fg = COLOR_RED, width=10).grid(row =2, column= 1)



root.resizable(False, False)
root.mainloop()
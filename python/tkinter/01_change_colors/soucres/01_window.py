from tkinter import *
from define import *
import os

root = Tk()

def setUpWindow():
    root.title('Change Colors')
    root.geometry('{}x{}+{}+{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_POS_RIGHT, WINDOW_POS_LEFT))

    root.iconbitmap(os.path.join(PATH_IMG, 'icon.ico'))

    root.configure(bg = COLOR_BG)

setUpWindow()

root.resizable(False, False)

root.mainloop()
from define import *
import os

class App():
    def __init__(self, window) -> None:
        window.title('Change Colors')
        window.geometry('{}x{}+{}+{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_POS_RIGHT, WINDOW_POS_LEFT))
        window.iconbitmap(os.path.join(PATH_IMG, 'icon.ico'))

        window.configure(bg = COLOR_BG)
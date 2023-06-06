import os
from tkinter import font
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
WINDOW_POS_RIGHT = 400
WINDOW_POS_LEFT = 200

COLOR_BG = 'blue'
COLOR_YELLOW = 'yellow'
COLOR_RED = 'red'

font_title = font.Font(family ="Stencil Std", size = 40)
font_text = font.Font(family ="Terminal", size = 20)

PATH_DIR = os.path.dirname(__file__)
PATH_IMG = os.path.join(PATH_DIR, 'images')
import pygame, sys
from pygame.locals import*
pygame.init()
DISPLAY = pygame.display.set_mode((500,400))
pygame.display.set_caption('COLOUR')
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DISPLAY.fill(WHITE)
# Vẽ hình ngũ giác có các đỉnh là các toạ độ dưới:
pygame.draw.polygon(DISPLAY, GREEN, ((146,0) , (291,106) , (236,277) , (56,277) , (0,106)))
# Vẽ đường thẳng nối 2 điểm có tọa độ dưới :
pygame.draw.line(DISPLAY, BLUE, (60,60) , (120,60), 4)
# Vẽ và tô hình tròn màu BLUE :
pygame.draw.circle(DISPLAY, BLUE, (300,100), 50, 0)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    

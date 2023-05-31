import pygame
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Học Toán Online')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 32)
dialogue_font = pygame.font.SysFont('utf8', 32)
running = True
bg = pygame.image.load(('IMG_111.jpg'))
bg = pygame.transform.scale(bg, (800, 700))
bando = pygame.image.load(('IMG_111.jpg'))
menu = pygame.image.load(('IMG_111.jpg'))
home = pygame.image.load(('IMG_111.jpg'))
home = pygame.transform.scale(home, (50, 50))
x = 'first'
clock = pygame.time.Clock()
font1 = pygame.font.SysFont('san', 80)
textstart = font.render("START ", True, BLACK)

while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pygame.draw.rect(screen, BLACK, (0, 0, 800, 600))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and (mouse_x > 300 and mouse_x < 500) and (mouse_y > 350 and mouse_y < 450) and x == 'first':
                x = 'bg'
    if x == 'first':
        pygame.draw.rect(screen, WHITE, (300, 350, 200, 100))
        screen.blit(textstart, (350, 380))
    if x == 'bg':
        screen.blit(bg, (0, 0))

    pygame.display.flip()
    clock.tick(120)

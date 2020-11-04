import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("pygame으로 내가 만드는 게임")
screen = pygame.display.set_mode((640, 650))

star_img = pygame.image.load("images/star.png").convert()

while True:
    clock.tick(60)

    # screen.fill((0,0,0))
    
    pos = pygame.mouse.get_pos()
    mx = pos[0]
    my = pos[1]

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(star_img, (mx,my))

    pygame.display.update()

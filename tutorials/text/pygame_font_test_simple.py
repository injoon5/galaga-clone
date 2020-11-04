import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("pygame으로 내가 만드는 게임")
screen = pygame.display.set_mode((640, 650))

# 글자체 None 으로 해놓으면, 기본폰트로 적용됨
myfont = pygame.font.Font(None, 50)
# myfont = pygame.font.SysFont("arialblack", 50)
# print(pygame.font.get_fonts())

score = 0

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill((0,0,0))

    score = score + 1
    score_img = myfont.render("Score : " + str(score), True, (255,255,255))
    screen.blit(score_img , (10, 10))

    pygame.display.update()


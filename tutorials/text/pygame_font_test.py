import pygame
from pygame.locals import *

score = "80"

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("pygame으로 내가 만드는 게임")

# 창크기 너비, 높이 지정
screen_width = 640
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))

# 글자체 None 으로 해놓으면, 기본폰트로 적용됨
myfont = pygame.font.Font(None, 50)

# myfont = pygame.font.SysFont("arialblack", 50)
# print(pygame.font.get_fonts())

while True:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    score_img = myfont.render("Score : " + score, True, (255,255,255))
    
    score_width = score_img.get_width()
    score_height = score_img.get_height()

    score_pos_x = (screen_width // 2) - (score_width // 2)
    score_pos_y = (screen_height // 2) - (score_height // 2)

    # print(score_img, score_width, score_height, score_pos_x, score_pos_y)

    screen.blit(score_img , (score_pos_x, score_pos_y))

    pygame.display.update()


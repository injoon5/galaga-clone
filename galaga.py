import pygame, sys, random
from pygame.locals import *



class Enermy:
      def __init__(self):
            self.x = random.randint(0, 570)
            self.y = -100
            self.dy = 0
            self.dx = 3
      def move(self):
            if self.x>570 or self.x<0:
                  self.dx = -(self.dx)
           
            self.dy += 0.1
            self.y += self.dy
            self.x += self.dx
      def draw(self):
            screen.blit(enermy_image, (self.x, self.y))
      def off_screen(self):
            return self.y > 640

enermy = Enermy()

pygame.init()
pygame.display.set_caption("Galaga")
screen = pygame.display.set_mode((640, 650))

enermy_image = pygame.image.load("images/enemy.png").convert()

clock = pygame.time.Clock()
while 1:
      clock.tick(60)
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  sys.exit

      screen.fill((0, 0, 0))
      enermy.move()
      enermy.draw()
      pygame.display.update()

